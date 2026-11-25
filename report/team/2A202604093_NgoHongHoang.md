# Báo cáo cá nhân — Ngô Hồng Hoàng - 2A202604093

## 1. Thông tin thành viên

- Họ tên: Ngô Hồng Hoàng
- MSSV: 2A202604093
- Email: honghoangngo@gmail.com
- Vai trong nhóm: Người kiểm số
- GitHub: HoangHongNgo

## 2. Phần việc phụ trách

Tính tay một con số để đối chiếu (ví dụ 4.472 đ, 16,3×, n = 859) và điền `bang_chi_phi.md`, `pilot_plan.yaml`.

## 3. Đóng góp cụ thể

- Nhận repo đề bài, fork về tài khoản HoangHongNgo, điền tên nhóm Economics và đẩy các commit hồ sơ lên `main`.
- Người kiểm số: tính tay, không qua `lab13.py`, các con số then chốt để đối chiếu với kết quả của code (bảng bên dưới).
- Điền và rà `bang_chi_phi.md` (A1–B4) và `pilot_plan.yaml` (D1, D2, luật dừng); kiểm tra `pilot_plan.yaml` đọc được bằng `yaml.safe_load` và không còn dấu `?` ngoài dòng chú thích.
- Kiểm tra cả bộ hồ sơ không dùng từ bị cấm theo quy tắc 5 của lab và mọi số tính từ cột `_simulated` có nhãn simulated.

| Con số | Tính tay | Kết quả `lab13.py` |
| --- | --- | --- |
| Chi phí mỗi việc thành công | 4.373.585 ÷ 978 = 4.471,97 ≈ 4.472 đ | 4.472 đ |
| Gấp bao nhiêu lần hoá đơn token | 4.472 ÷ 274,7 = 16,3 | 16,3× |
| Chi phí cả hệ thống mỗi yêu cầu | (4.373.585 + 222 × 12.000) ÷ 1.200 = 5.864,65 | 5.865 đ (0,49×) |
| Chi phí cố định mỗi việc, 45.000 yêu cầu/tháng | 40.000.000 ÷ 33.750 = 1.185,19; 3.414 + 1.185 = 4.599 | 4.599 đ (0,38×) |
| Cỡ mẫu mỗi nhóm, chênh 5 điểm | công thức z = 1,96 và 0,8416 cho 1.250,7 | 1.251 |
| Xem lại 100% (noi_dia + hang_nang) | 9.480.000 + 864.000 + 224.513 = 10.568.513; ÷ 900 = 11.742,8 | 11.743 đ (0,98×) |

Tất cả lệch dưới 0,1%, trong ngưỡng 2% của lab. Các số tiền xem lại, làm lại và chi phí mỗi việc là [simulated].

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- Commit: `6fa2b3d` (lab13.py, hồ sơ A–E), `0ddd709` (tên nhóm), `69e2c74` (cập nhật mục 5 hồ sơ), `6fb7f1b` (commit bằng chứng trong TEAM.md).
- File: `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml`, bảng đối chiếu ở mục 3.

## 5. Công cụ AI đã dùng

Claude Code: nhóm dùng để viết code `lab13.py` và soạn nháp các file hồ sơ. Kết quả được đối chiếu với số mẫu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch dưới 2%) và chạy lại `python lab13.py`. Cách tự kiểm tra: tính tay sáu con số ở mục 3 độc lập với code, chạy lại `python lab13.py` và đối chiếu số mẫu trong hướng dẫn; không dùng AI để bịa số hay nhãn lỗi.

## 6. Tự đánh giá

Điểm mạnh: mọi con số then chốt đều được đối chiếu bằng tay và khớp. Điểm cần cải thiện: nhãn lỗi 20 ca chưa gắn độc lập thuần túy (xem `bang_loi.md`), và phút xem lại, làm lại vẫn là số giả lập, cần thay bằng phút đo thật sau tuần 1 của pilot.
