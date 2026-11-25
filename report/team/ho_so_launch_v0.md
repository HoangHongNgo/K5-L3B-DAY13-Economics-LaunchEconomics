# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Gate 2a chỉ duyệt kế hoạch pilot.

Nhóm: Economics · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ [simulated], gấp 16,3× hoá đơn token+tool/yêu cầu (274,7 đ); làm lại 51,8% + xem lại 40,7% tổng chi phí | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. số ca làm lại ±51,8% · 2. tỉ lệ xem lại ±40,7% · 3. lương +23,1%; giá token chỉ +5,6% [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống 5.865 đ/yêu cầu = 0,49× của 12.000 đ [simulated]; phạm vi noi_dia + hang_nang cộng cố định 4.599 đ = 0,38×; quoc_te 1,88× nên loại; xem lại 100% = 0,98× (1,03× với phút làm lại thực) | Giả lập | Giám đốc tài chính |
| 4 · Chỉ số chính, dùng, an toàn | Chính 82,83% · bỏ qua gợi ý 27,12% (48/177) · mở lại 7 ngày 4,25%; đủ 10 event có trace_id | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca, 5 loại; 5 ca khắc phục, mỗi dòng có ngưỡng đo được; đồng thuận nhãn 20/20 = 100%, nhưng hai bộ nhãn có tham khảo AI nên chưa độc lập thuần túy (xem `bang_loi.md`) | Chưa (cần gắn lại độc lập) | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo 20 + 20 nhân viên, n = 859 mỗi nhóm, DE 6,96, chênh phát hiện 6 điểm (power 0,64 nếu thật là 5 điểm); 4 luật dừng, bước 20 người cần 8 ngày gom đủ đơn, quyết định 2027-01-05 | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi +51,8% (6.787 đ); xem lại 100% = 0,98×; cố định +1.185 đến +2.370 đ/việc [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** cho pilot noi_dia + hang_nang (loại quoc_te và doi_tac). Điều kiện:

1. Sửa khoá chống trùng và đối soát sổ cái (ca 7, 20) trước ngày bắt đầu pilot. Phụ trách: Kỹ sư trưởng agent. Kiểm tra: 2026-12-15.
2. Giám đốc vận hành ký chấp nhận mức chênh 6 điểm (power chỉ 0,64 ở mức 5 điểm). Phụ trách: Giám đốc vận hành. Kiểm tra: 2026-12-20.
3. Bật đủ event có trace_id; thay phút simulated bằng phút đo thật sau tuần 1. Phụ trách: PM trợ lý hoàn phí. Kiểm tra: tuần 1 của pilot.
4. Có kế hoạch giảm xem lại theo bậc, vì xem lại 100% gần như không tiết kiệm (0,98×, B4) [simulated]. Phụ trách: Trưởng nhóm CSKH. Kiểm tra: cuối bước rollout 0.25.
