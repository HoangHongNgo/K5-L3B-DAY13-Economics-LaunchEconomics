# Team

## Thông tin nhóm

- Tên nhóm: Economics
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Economics-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/HoangHongNgo/K5-L3B-DAY13-Economics-LaunchEconomics · main · commit chốt hiện tại 69e2c74 (cập nhật nếu còn thay đổi)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Minh Triết | 2A202603995 | mtriet674@gmail.com | minhtriet061203 | Người viết code |
|   2 | Ngô Hồng Hoàng | 2A202604093 | honghoangngo@gmail.com | HoangHongNgo | Người kiểm số |
|   3 | Hoàng Minh | 2A202604103 | minh03forwork@gmail.com | WorkOfMinh | Người gắn nhãn 1 |
|   4 | Nguyễn Việt Hoàng | 2A202604104 | [điền] | [điền] | Người gắn nhãn 2 kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## NguyenMinhTriet-2A202603995

### Phần việc phụ trách

- Người viết code: Viết và chạy `src/lab13.py` (A1, `mo_hinh`, A3, A4, B1–B4, D1, E1); đổi người viết code sau giờ giải lao.

### Đóng góp cụ thể

- Viết toàn bộ `src/lab13.py`: ba hàm A1 (ba phép thử ĐẠT 1,20 · 1,25 · 1,25), `mo_hinh` (4.472 đ/việc thành công [simulated], 16,3× hoá đơn), A3, A4, B1–B4, `co_mau` cho D1 (n = 1.251; MDE 6 điểm → n = 859) và ba chỉ số E1.
- Chạy lại toàn bộ code trên máy cá nhân (venv sạch, Python 3.12.10): chạy hết, số khớp `bang_chi_phi.md`.

### Bằng chứng

- `report/team/2A202603995_NguyenMinhTriet.md`; `src/lab13.py` (gộp và commit qua tài khoản HoangHongNgo ở 6fa2b3d); commit cập nhật báo cáo từ tài khoản minhtriet061203

## NgoHongHoang-2A202604093

### Phần việc phụ trách

- Người kiểm số: Tính tay một con số để đối chiếu (ví dụ 4.472 đ, 16,3×, n = 859) và điền `bang_chi_phi.md`, `pilot_plan.yaml`.

### Đóng góp cụ thể

- Fork repo, điền tên nhóm, đẩy các commit hồ sơ lên `main`.
- Kiểm tay sáu con số then chốt (4.472 đ, 16,3×, 5.865 đ, 4.599 đ, n = 1.251, 11.743 đ), lệch dưới 0,1% so với `lab13.py`.
- Rà `bang_chi_phi.md`, `pilot_plan.yaml`; kiểm tra YAML hợp lệ, không dấu `?`, không dùng từ bị cấm theo quy tắc 5 của lab.

### Bằng chứng

- `report/team/2A202604093_NgoHongHoang.md`; commit: 6fa2b3d, 0ddd709, 69e2c74 (tài khoản HoangHongNgo)

## HoangMinh-2A202604103

### Phần việc phụ trách

- Người gắn nhãn 1: Gắn nhãn độc lập 20 ca lỗi ở CP3, theo dõi điều kiện "Xong khi", điền `bang_loi.md` (bảng khắc phục) và `chi_so.md`.

### Đóng góp cụ thể

- CP3: Phân loại 20 ca lỗi theo 5 loại lỗi của Google PAIR và điền cột "Nhãn người 1" trong bang_loi.md.

- Rà soát quy tắc phân biệt các loại lỗi và bảng khắc phục cho 5 ca, mỗi loại một ca.

- Chuẩn bị đối chiếu kết quả gắn nhãn với người gắn nhãn 2 và tính tỉ lệ đồng thuận.

### Bằng chứng

- `report/team/2A202604103_HoangMinh.md`; commit: 2bf2e89 (nhánh HoangMinh)

## NguyenVietHoang-2A202604104

### Phần việc phụ trách

- Người gắn nhãn 2 kiêm giữ hồ sơ: Gắn nhãn độc lập 20 ca lỗi ở CP3; giữ và điền `ho_so_launch_v0.md`, `group_report.md`, `phieu_cham.md`.

### Đóng góp cụ thể

- [Thành viên tự điền]

### Bằng chứng

- `report/team/2A202604104_NguyenVietHoang.md`; commit: 2235e50 (viethoang126)

