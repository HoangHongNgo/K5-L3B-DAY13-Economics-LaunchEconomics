# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py` (chạy `python lab13.py` trong `src/`). Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 (ĐẠT) |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 (ĐẠT) |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 = 1/p (ĐẠT) |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token (mọi lần chạy, kể cả lần lỗi) | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool (5.600 lần gọi × 15 đ) | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại (890 phút × 2.000 đ) | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại (1.132 phút × 2.000 đ) | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | có phần simulated |
| Số việc thành công (mẫu số) | 978 | `ket_qua == thanh_cong` | đo từ dữ liệu |
| Chi phí mỗi việc thành công | 4.472 | tổng ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (245.585 + 84.000) ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp **16,3 lần** "hoá đơn chia số yêu cầu" (4.472 ÷ 274,7) [simulated].
- Khoản lớn nhất là **làm lại: 51,8%** tổng chi phí [simulated]; tiếp theo xem lại 40,7% [simulated]. Giờ nhân viên chiếm 92,5%, token + tool chỉ 7,5%.
- So với nhân viên tự làm, phải tính cả phần nhân viên làm thay 222 yêu cầu không thành công: (4.373.585 + 222 × 12.000) ÷ 1.200 = **5.865 đ/yêu cầu = 0,49×** của 12.000 đ [simulated]. Con số 4.472 đ chưa gồm phần này nên không so thẳng với 12.000 đ.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công [simulated] | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

Tỉ lệ `ok` theo lần chạy (đo từ trace): noi_dia 91,0% → 75,7% → 38,9%; hang_nang 70,9% → 39,1% → 17,9%; doi_tac 51,5% → 18,2% → 14,8%; quoc_te 30,0% → 11,4% → 2,2%.

- **quoc_te không đáng để trợ lý xử lý**: 1,88× chi phí nhân viên [simulated], thành công 27,3%. Chạy lại tới 3 lần không giúp: tỉ lệ ok giảm 30,0% → 11,4% → 2,2%, lỗi lặp lại trên cùng yêu cầu nên chỉ tốn thêm tiền.
- doi_tac sát ngưỡng (0,85× [simulated]) và có điều khoản riêng, nên cũng loại khỏi phạm vi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Chi phí mỗi việc thành công trong phạm vi (chưa cố định) = 3.414 đ [simulated]; phạm vi chiếm 982/1.200 yêu cầu, 900 việc thành công.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định [simulated] | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

- Chi phí cố định 40 triệu đ/tháng không đổi kết luận ở khối lượng đầy đủ (0,38×) và cả khi chỉ còn một nửa (0,48×), vẫn dưới 1×. Nhưng nó làm chi phí mỗi việc tăng +1.185 đến +2.370 đ khi khối lượng nhỏ, nên hồ sơ phải ghi rõ con số đã cộng cố định ở khối lượng nào.

## B1 · Đổi từng yếu tố

Chi phí gốc: 4.472 đ [simulated].

| Kịch bản | Cách tính | Chi phí mỗi việc thành công [simulated] | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 | −8,1% |

Tự kiểm tra: mỗi kịch bản "giảm một nửa" bằng đúng nửa mức tăng của "gấp đôi" (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9).

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%)** [simulated] = 5,6 + 40,7, vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. **số ca làm lại** (±51,8%) · 2. **tỉ lệ xem lại** (±40,7%) · 3. **lương nhân viên** (+23,1%). Giá token chỉ +5,6%.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công (nhân viên làm thay) [simulated].

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 | 319 | 7.449.781 | 4.111 (thấp nhất) |
| 2 lần | 4.093.220 | 234 | **6.901.220 (rẻ nhất)** | 4.237 |
| 3 lần | 4.373.585 | 222 | 7.037.585 | 4.472 |

- Giới hạn **2 lần** rẻ nhất cho công ty (6.901.220 đ). Không trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất (1 lần, 4.111 đ): giới hạn 1 lần đẩy thêm 85 yêu cầu sang nhân viên và tổng cả hệ thống đắt hơn 548.561 đ.

## B4 · Nếu phải xem lại tất cả

Phạm vi noi_dia + hang_nang (982 yêu cầu): 948 yêu cầu có ít nhất một lần chạy ok × 5 phút xem lại; 48 ca lam_lai; token + tool 224.513 đ; 900 việc thành công.

- Xem lại 100%: **11.743 đ = 0,98×** của 12.000 đ [simulated] (làm lại 9 phút/ca theo đề). Nếu dùng phút làm lại thật của 48 ca trong phạm vi (16,2 phút/ca): 12.516 đ = 1,04× [simulated]; theo cả mẫu (15,3 phút/ca, trung bình mọi ca lam_lai) ra 12.414 đ = 1,03×. Hoà vốn khi mỗi lần xem lại ≤ 5,1 phút (9 phút làm lại) hoặc ≤ 4,8 phút (phút làm lại thực).
- Pilot phải học được **tỉ lệ xem lại có thể giảm an toàn xuống mức nào** và mỗi lần xem lại có ngắn hơn 5 phút được không: xem lại 100% thì trợ lý gần như không tiết kiệm (tiền xem lại chiếm ~90% chi phí) [simulated].
