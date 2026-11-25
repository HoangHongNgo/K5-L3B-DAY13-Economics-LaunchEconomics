# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

> **CẦN NHÓM LÀM THẬT (theo RULES.md):** hai cột "Nhãn người 1" và "Nhãn người 2" phải do hai thành viên gắn **độc lập, không trao đổi** rồi điền vào. Cột "Nhãn thống nhất" bên dưới là nhãn đề xuất đã phân tích theo định nghĩa nguyên nhân gốc, dùng để đối chiếu sau khi hai người đã gắn xong. Không sửa hai cột độc lập sau khi so.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: [điền tên] · Người gắn nhãn 2: [điền tên] (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất (đề xuất) |
| --: | --- | --- | --- | --- |
| 1 | [điền] | [điền] | [điền] | Do người dùng |
| 2 | [điền] | [điền] | [điền] | Hệ thống |
| 3 | [điền] | [điền] | [điền] | Ngữ cảnh |
| 4 | [điền] | [điền] | [điền] | Giới hạn hệ thống |
| 5 | [điền] | [điền] | [điền] | Ngầm |
| 6 | [điền] | [điền] | [điền] | Do người dùng |
| 7 | [điền] | [điền] | [điền] | Hệ thống |
| 8 | [điền] | [điền] | [điền] | Hệ thống |
| 9 | [điền] | [điền] | [điền] | Do người dùng |
| 10 | [điền] | [điền] | [điền] | Ngữ cảnh |
| 11 | [điền] | [điền] | [điền] | Giới hạn hệ thống |
| 12 | [điền] | [điền] | [điền] | Ngầm |
| 13 | [điền] | [điền] | [điền] | Giới hạn hệ thống |
| 14 | [điền] | [điền] | [điền] | Do người dùng |
| 15 | [điền] | [điền] | [điền] | Hệ thống |
| 16 | [điền] | [điền] | [điền] | Ngữ cảnh |
| 17 | [điền] | [điền] | [điền] | Ngầm |
| 18 | [điền] | [điền] | [điền] | Ngữ cảnh |
| 19 | [điền] | [điền] | [điền] | Giới hạn hệ thống |
| 20 | [điền] | [điền] | [điền] | Hệ thống |

Phân bố nhãn đề xuất: Do người dùng 4 (1, 6, 9, 14) · Hệ thống 5 (2, 7, 8, 15, 20) · Ngữ cảnh 4 (3, 10, 16, 18) · Giới hạn hệ thống 4 (4, 11, 13, 19) · Ngầm 3 (5, 12, 17).

**Tỉ lệ đồng thuận:** [điền] / 20 = [điền]% (ngưỡng đạt: 16/20 = 80%)

## Quy tắc phân biệt cho các ca dễ lẫn

Mỗi ca không trùng một câu (điền thêm nếu hai người gắn khác nhau ở ca khác). Các ca dễ lẫn nhất:

- **Ca 6, 9 là Do người dùng, không phải Hệ thống:** gốc lỗi là khách chọn sai mục hoặc nhập sai mã; việc trợ lý không gợi ý lại là chỗ cần cải thiện, ghi ở cột khắc phục.
- **Ca 13 là Giới hạn hệ thống:** ngoài phạm vi thì là giới hạn, kể cả khi trợ lý xử lý giới hạn đó kém.
- **Ca 8, 15 là Hệ thống, không phải Ngầm:** sai đã lộ ra (trích dẫn nhìn thấy được; nhân viên bắt được trước khi gửi). Ngầm chỉ dùng khi không ai nhận ra cho tới khi kiểm tra.
- **Ca 18 là Ngữ cảnh:** số tiền đúng chính sách, chỉ giả định "khách hiểu cách tính" không khớp hoàn cảnh.
- **Ca 12 là Ngầm:** câu trả lời đúng nhưng chi phí gấp 3 lần suốt 3 tuần mà không ai thấy; "sai" có thể là sai về chi phí.
- **Ca 3, 10, 16 là Ngữ cảnh:** hệ thống làm đúng thiết kế, chỉ kỳ vọng của khách không khớp.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo khi vượt 2% số yêu cầu/ngày | Nhận diện mã sàn TMĐT và tra sang mã vận đơn; không tra được thì hướng dẫn kèm ảnh chỗ tìm mã | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: tin nhắn "đã hoàn" mà không có bản ghi sổ cái `ok` cùng `trace_id`; ngưỡng 0 ca | Chỉ báo "đã hoàn" khi sổ cái trả ok; lỗi 503 sau 3 lần thì báo "đang xử lý" và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ mở lại với lý do "số tiền" mà kiểm tra thấy đúng, theo tuần; ngưỡng 1% số ca hoàn | Mẫu tin nhắn luôn ghi cách tính: 30.000 đ × 50% = 15.000 đ | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = thieu_du_lieu`, theo loại yêu cầu, báo cáo tuần | Giữ cách chuyển kèm tóm tắt; loại yêu cầu thiếu dữ liệu (quoc_te) ra khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn/tuần so với bảng giá hiện hành (event `audit_sample_checked`); ngưỡng 1% đơn lệch | Xoá bộ nhớ đệm khi có bảng giá mới; ghi phiên bản bảng giá vào trace | Kế toán trưởng |
