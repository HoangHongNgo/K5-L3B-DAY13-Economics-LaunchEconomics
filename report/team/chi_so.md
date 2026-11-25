# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12%** (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51/1.200) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhân viên nhóm can thiệp được mở bằng trợ lý | số yêu cầu có `agent_suggestion_shown` chia số yêu cầu của nhóm can thiệp, theo tuần | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17) | `so_tien_da_hoan` khác `so_tien_dung` trong mẫu 100 đơn/tuần | Không cần tính |

Chỉ số trong đợt chạy thử là 82,83% (đợt chạy thử không có nhóm đối chứng, nên không kết luận trợ lý đã nâng chỉ số so với mốc 0,70).

## Danh sách event

Mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien, arm, trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra |
| `staff_review_decision` | Nhân viên | quyet_dinh (giu/sua/bo), phut_xem_lai (đo thật), trace_id | Khi bấm gửi/sửa/bỏ |
| `staff_rework_completed` | Nhân viên | phut_lam_lai, ly_do, trace_id | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ |
| `handoff_to_staff` | Agent | reason, tom_tat, trace_id | Khi chuyển nhân viên |
| `ticket_closed` | Hệ thống ticket | closed_at, trace_id | Khi đóng |
| `ticket_reopened` | Khách | reopened_at, reason, trace_id | Khi mở lại |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần |

**Kiểm tra chéo (chỉ số → event dùng để tính):**

- Chỉ số chính: `refund_request_created` (mẫu số), `ticket_closed` (đóng trong 24 giờ), `ticket_reopened` (mở lại trong 7 ngày).
- Dùng (bỏ qua gợi ý): `agent_suggestion_shown`, `staff_review_decision`. Dùng tự đề xuất: `refund_request_created` (có thuộc tính `arm`) và `agent_suggestion_shown`.
- An toàn (mở lại): `ticket_reopened` trên `refund_request_created`. An toàn tự đề xuất: `audit_sample_checked`.
- Chi phí mỗi việc thành công: `agent_run_completed`, `staff_review_decision`, `staff_rework_completed`, `handoff_to_staff`. Mọi chỉ số đều tính được từ danh sách event này.
- Phút xem lại và làm lại hiện là số simulated; sau tuần 1 thay bằng phút đo thật từ `staff_review_decision` và `staff_rework_completed`.

## E2 · Rủi ro kinh tế

Số lấy từ bảng độ nhạy trong `bang_chi_phi.md` (tất cả [simulated]).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, lên 6.787 đ mỗi việc thành công [simulated] | Tỉ lệ làm lại theo tuần vượt 7% (đợt chạy thử: 4,9% trong phạm vi) | Thu hẹp về noi_dia, rà 20 trace làm lại | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× của 12.000 đ (12.414 đ = 1,03× nếu làm lại 15,3 phút như trong dữ liệu) [simulated] | % yêu cầu được xem lại còn trên 50% cuối bước 0.25 | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ dưới 15% | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng, +2.370 đ/việc nếu còn một nửa [simulated] | Số việc thành công theo tuần dưới 50% kế hoạch | Không mở rộng pilot; xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
| Lương nhân viên tăng 25% | +23,1%, lên 5.506 đ [simulated] | Đơn giá phút nhân viên theo quý | Cập nhật mô hình chi phí trước mỗi cổng duyệt | Giám đốc tài chính |
