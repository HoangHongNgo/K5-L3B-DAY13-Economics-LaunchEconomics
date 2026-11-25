# Báo cáo cá nhân — Nguyễn Việt Hoàng - 2A202604104

## 1. Thông tin thành viên

- Họ tên: Nguyễn Việt Hoàng
- MSSV: 2A202604104
- Email: hoangnv0810@gmail.com
- Vai trò trong nhóm: Người gắn nhãn 2 kiêm giữ hồ sơ

## 2. Phần việc phụ trách

Gắn nhãn độc lập 20 ca lỗi ở CP3; giữ và điền `ho_so_launch_v0.md`, `group_report.md`, `phieu_cham.md`.

## 3. Đóng góp cụ thể

- **Gắn nhãn 20 ca lỗi (CP3).** Đọc 20 ca trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` và gắn theo năm loại của Google PAIR, theo nguyên tắc nguyên nhân gốc. Phân bố nhãn của tôi: Do người dùng 4 (1, 6, 9, 14) · Hệ thống 5 (2, 7, 8, 15, 20) · Ngữ cảnh 4 (3, 10, 16, 18) · Giới hạn hệ thống 4 (4, 11, 13, 19) · Ngầm 3 (5, 12, 17). Đã ghi vào cột "Nhãn người 2" của `bang_loi.md`.
- **Các ca dễ lẫn và lý do chọn nhãn:**
  - Ca 6, 9 là Do người dùng: gốc lỗi là khách chọn sai mục hoặc nhập sai mã; việc trợ lý không gợi ý chỉ là chỗ cần cải thiện ở cột khắc phục.
  - Ca 8, 15 là Hệ thống, không phải Ngầm: sai đã lộ ra (trích dẫn nhìn thấy được; nhân viên bắt được trước khi gửi).
  - Ca 13 là Giới hạn hệ thống: ngoài phạm vi thì là giới hạn, dù trợ lý trả lời chung chung.
  - Ca 18 là Ngữ cảnh: số tiền đúng chính sách (30.000 đ × 50% = 15.000 đ), chỉ thiếu cách tính.
  - Ca 12 là Ngầm: câu trả lời đúng nhưng chi phí gấp 3 lần suốt 3 tuần mà không ai thấy.
- **Giữ hồ sơ.** Rà `ho_so_launch_v0.md` (7 mục, đề xuất Go có điều kiện), `group_report.md`, `phieu_cham.md`; xác định phần còn thiếu (đồng thuận nhãn, kết quả duyệt chéo, phiếu chấm) và đối chiếu số trong hồ sơ với slide đáp án.
- **Đọc slide để chuẩn bị debate Gate 2a:** thang chấm 30 điểm, ba câu hội đồng hay hỏi (đo thật hay giả lập, xem lại gấp đôi còn đáng không, ai có quyền dừng), và lưu ý ca 6, 13 có thể được lập luận sang nhãn khác.
- **Việc chưa xong tại thời điểm viết:** chưa có bộ nhãn độc lập của Người gắn nhãn 1 (Hoàng Minh) nên chưa tính được tỉ lệ đồng thuận thật; chưa điền `phieu_cham.md`; mục 5 của `ho_so_launch_v0.md` vẫn là "Chưa".

## 4. Bằng chứng

- Commit `2235e50` trên `main`: điền nhãn người 2, tên hai người gắn nhãn và ghi chú minh bạch trong `report/team/bang_loi.md`.
- File: `report/team/bang_loi.md` (cột "Nhãn người 2").
- [Bổ sung commit của các file hồ sơ khác sau khi điền.]

## 5. Công cụ AI đã dùng

Claude Code: nhóm dùng để viết code `lab13.py` và soạn nháp các file hồ sơ. Kết quả được đối chiếu với số mẫu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch dưới 2%) và chạy lại `python lab13.py`.

Phần của tôi: Claude Code đọc 20 ca lỗi và đề xuất nhãn cho cột "Nhãn người 2". Cần nói rõ: lúc đó Claude Code đã xem bảng nhãn tham khảo trong hướng dẫn, nên bộ nhãn này **không phải bộ nhãn độc lập thuần túy**. Tôi đã ghi chú điều này ngay trên bảng trong `bang_loi.md`. Số đồng thuận chính thức phải lấy từ so sánh với nhãn độc lập của Hoàng Minh.

Cách tự kiểm tra của tôi: tự gắn lại 20 ca không nhìn bảng rồi liệt kê ca khác nhãn; chạy lại `python lab13.py` và so với bảng mẫu.

## 6. Tự đánh giá

- Làm tốt: hiểu quy tắc gắn nhãn theo nguyên nhân gốc và lập luận được các ca dễ lẫn; nắm thang chấm Gate 2a để chuẩn bị bảo vệ; ghi rõ giới hạn của nhãn có AI hỗ trợ thay vì che giấu.
- Chưa tốt: nhãn của tôi chưa được gắn hoàn toàn độc lập; tỉ lệ đồng thuận, phiếu chấm và kết quả duyệt chéo còn thiếu.
- Sẽ làm tiếp: so nhãn với Hoàng Minh, điền đồng thuận, cập nhật mục 5 hồ sơ launch, điền `phieu_cham.md` và `group_report.md` sau buổi duyệt chéo.


