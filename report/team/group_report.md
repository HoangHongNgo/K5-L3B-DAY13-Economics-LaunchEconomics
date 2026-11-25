# Báo cáo nhóm

## 1. Thông tin nhóm

- Tên nhóm: Economics
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Trả lời bốn câu cho trợ lý hoàn phí LogiX-VN: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào. Dữ liệu là 1.200 yêu cầu / 1.624 lần chạy, toàn bộ giả lập; mọi số tính từ cột `_simulated` có nhãn `simulated`.

## 3. Giải pháp

- A, B: `src/lab13.py` (ba phép thử A1 đạt; `mo_hinh` dùng lại cho A3, A4 và 9 kịch bản độ nhạy) → [bang_chi_phi.md](bang_chi_phi.md).
- C: 20 ca lỗi vào 5 loại PAIR, bảng khắc phục 5 ca → [bang_loi.md](bang_loi.md).
- D: cỡ mẫu và kế hoạch pilot → [pilot_plan.yaml](pilot_plan.yaml).
- E: chỉ số, event, rủi ro, hồ sơ → [chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md).

## 4. Kết quả

- Chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3× hoá đơn token+tool; giờ nhân viên chiếm 92,5%.
- noi_dia 0,22×, hang_nang 0,69×, doi_tac 0,85×, quoc_te 1,88× so với 12.000 đ [simulated] → pilot chỉ noi_dia + hang_nang.
- Nhạy nhất: số ca làm lại (±51,8%), tỉ lệ xem lại (±40,7%), lương (+23,1%). Giới hạn 2 lần chạy rẻ nhất cả hệ thống (6.901.220 đ).
- Pilot 20 + 20 nhân viên chỉ đủ mẫu cho chênh 6 điểm (n = 859, DE 6,96); power 0,64 nếu tác động thật là 5 điểm.
- Đề xuất: **Go có điều kiện**. Kết quả duyệt chéo: [điền sau buổi duyệt chéo].

## 5. Khó khăn và cách xử lý

- Cài thư viện lần đầu chậm (hơn 2 phút) trên Windows; chạy nền rồi tiếp tục.
- Phút làm lại thực (15,3 phút/ca) khác 9 phút của đề, làm B4 từ 0,98× thành 1,03×; báo cáo cả hai.

## 6. Tổng hợp đóng góp

Chi tiết nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Chi phí xem lại và làm lại là số giả lập; cần thay bằng phút đo thật sau tuần 1 của pilot.
- Đợt chạy thử không có nhóm đối chứng nên không kết luận trợ lý đã nâng chỉ số chính.
- Nhãn lỗi cần hai thành viên gắn độc lập để có tỉ lệ đồng thuận thật.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass*, arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, "Errors + Graceful Failure"
- Tài liệu statsmodels, `NormalIndPower`
