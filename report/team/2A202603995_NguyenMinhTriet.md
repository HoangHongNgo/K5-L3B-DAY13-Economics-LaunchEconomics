# Báo cáo cá nhân — Nguyễn Minh Triết - 2A202603995

## 1. Thông tin thành viên

- Họ tên: Nguyễn Minh Triết
- MSSV: 2A202603995
- Email: mtriet674@gmail.com
- GitHub: minhtriet061203
- Vai trong nhóm: Người viết code

## 2. Phần việc phụ trách

Viết và chạy `src/lab13.py` (A1, `mo_hinh`, A3, A4, B1–B4, D1, E1); xuất số cho người kiểm số chép vào `report/team/bang_chi_phi.md` và `pilot_plan.yaml`.

## 3. Đóng góp cụ thể

- **A1:** viết `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`; ba phép thử in ĐẠT (1,20 · 1,25 · 1,25).
- **A2 – `mo_hinh`:** tử số cộng token và tool trên **mọi** lần chạy (kể cả lần lỗi) cộng phút xem lại, làm lại × lương [simulated]; mẫu số chỉ đếm yêu cầu `ket_qua == thanh_cong`. Thêm tham số `he_so_xem_lai`, `he_so_lam_lai`, `max_lan_chay` để CP2 gọi lại cùng một hàm. Kết quả: tổng 4.373.585 đ ÷ 978 = **4.472 đ** [simulated], gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu (274,7 đ).
- **A3, A4:** tách theo loại (quoc_te 1,88× [simulated], tỉ lệ ok theo lần thử 30,0% → 11,4% → 2,2%); chi phí cố định 40 triệu đ/tháng cho phạm vi noi_dia + hang_nang: 0,38× và 0,48× [simulated].
- **B1–B4:** 9 kịch bản độ nhạy, cặp B2 (+46,3%), so giới hạn chạy theo chi phí cả hệ thống (giới hạn 2 lần rẻ nhất: 6.901.220 đ) và xem lại 100% (0,98× [simulated], hoà vốn ≤ 5,1 phút).
- **D1:** hàm `co_mau` (công thức hai tỉ lệ) → n = 1.251 mỗi nhóm; hệ số thiết kế 1 + (m − 1)·ICC; MDE 6 điểm → n = 859, m ≥ 299 yêu cầu/người; power còn 0,64 nếu tác động thật chỉ 5 điểm (dùng `statsmodels`).
- **E1:** ba chỉ số tính thử: chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại 7 ngày 4,25% (51/1.200).
- Chạy lại toàn bộ `python lab13.py` trên máy cá nhân (Windows, Python 3.12.10, venv mới cài từ `requirements.txt`): chạy hết, mọi số khớp `bang_chi_phi.md` — đáp ứng mục checklist "chạy hết trên một máy khác trong nhóm".

## 4. Bằng chứng

- File: `src/lab13.py` (code do tôi viết; được gộp và commit lên repo qua tài khoản HoangHongNgo ở commit `6fa2b3d`).
- Commit cá nhân: commit cập nhật báo cáo này và mục của tôi trong `TEAM.md` (tài khoản minhtriet061203).
- Con số do code của tôi in ra và được chép vào hồ sơ: 4.472 đ, 16,3×, bảng A3, B1 (9 dòng), B3, B4, n = 1.251 / 859, ba chỉ số E1.

## 5. Công cụ AI đã dùng

- **Claude Code:** gợi ý code `lab13.py`, giải thích công thức cỡ mẫu theo cụm, soạn nháp báo cáo này.
- **Cách tự kiểm tra:**
  - Tính tay A1 với p = 0,8: tối đa 2 lần → 1 + 0,2 = 1,20; chạy đến khi đúng → 1/0,8 = 1,25; tối đa 3 lần → số lần chạy (1 − 0,2³)/0,8 = 1,24, tỉ lệ thành công 0,992 → 1,24/0,992 = 1,25.
  - Kiểm tra tính cộng tuyến của mô hình: mỗi kịch bản "giảm một nửa" ở B1 bằng đúng nửa mức "gấp đôi" (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9), và B2 = 5,6 + 40,7 = 46,3%.
  - Đối chiếu với số mẫu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (4.472 đ, 16,3×, n = 859), lệch dưới 2%.
  - Chạy lại trên máy khác trong venv sạch để chắc code không phụ thuộc môi trường riêng.

## 6. Tự đánh giá

- **Làm tốt:** code chạy hết từ đầu đến cuối, ba phép thử đạt, các con số dùng chung một hàm `mo_hinh` nên B1–B4 nhất quán với A2. Tôi giải thích được vì sao tử số tính mọi lần chạy (lần lỗi vẫn tốn token và tool) còn mẫu số chỉ đếm việc thành công (đó là thứ công ty thực sự nhận được), và vì sao chia theo cụm làm cỡ mẫu hiệu dụng giảm theo hệ số thiết kế 1 + (m − 1)·ICC.
- **Cần cải thiện:** code được commit qua tài khoản của bạn trong nhóm nên lịch sử git không thể hiện trực tiếp phần của tôi; lần sau tôi sẽ tự commit từng checkpoint. Phần in kết quả còn dạng text thô, nên có thể in thẳng thành bảng Markdown để giảm lỗi khi chép số.
