"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python lab13.py   (cần pandas, statsmodels)
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập (simulated).
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist

import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
ICC = 0.02


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × lương phút. Đây là số simulated.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong' (mẫu số).
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:  # B1, B3: yêu cầu cần nhiều lần hơn giới hạn -> chuyển nhân viên
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ (chia theo yêu cầu, chưa tính cụm)."""
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def nhiem_vu_a(runs, reqs):
    ket_qua = mo_hinh(runs, reqs)
    print('\n== A2 (đ) ==')
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:15s} {gia_tri:>14,.1f}')
    goc = ket_qua['cps']
    print(f"Gấp {goc / ket_qua['hoa_don_moi_yc']:.1f} lần hoá đơn token+tool/yêu cầu [simulated]")
    print(f"Làm lại {ket_qua['lam_lai'] / ket_qua['tong']:.1%}, xem lại {ket_qua['xem_lai'] / ket_qua['tong']:.1%} "
          f"tổng; giờ nhân viên {(ket_qua['lam_lai'] + ket_qua['xem_lai']) / ket_qua['tong']:.1%} [simulated]")

    print('\n== A3 theo loại [simulated] ==')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs.loai == loai]
        m = mo_hinh(runs, r)
        lan = runs[runs.request_id.isin(r.request_id)].shape[0] / len(r)
        print(f"{loai:10s} n={len(r):4d} thành công={m['thanh_cong'] / len(r):6.1%} lần/yc={lan:.2f} "
              f"cps={m['cps']:8,.0f} x{m['cps'] / BASELINE:.2f}")
    pv = (runs.merge(reqs[['request_id', 'loai']])
          .assign(ok=lambda d: d.status == 'ok')
          .pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean'))
    print('Tỉ lệ ok theo lần thử:\n', pv.round(3))

    print('\n== A4 chi phí cố định (noi_dia + hang_nang) [simulated] ==')
    m = mo_hinh(runs, reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])])
    sub_n = reqs.loai.isin(['noi_dia', 'hang_nang']).sum()
    print(f"cps trong phạm vi={m['cps']:,.0f}; tỉ lệ yêu cầu trong phạm vi={sub_n}/{len(reqs)}")
    for ten, khoi in [('45.000 yc/tháng', 45000), ('một nửa', 22500)]:
        viec = khoi * m['thanh_cong'] / len(reqs)
        cd = 40_000_000 / viec
        print(f"{ten}: việc/tháng={viec:,.0f} cố định/việc={cd:,.0f} → {m['cps'] + cd:,.0f} đ "
              f"(x{(m['cps'] + cd) / BASELINE:.2f})")
    n_ko = (reqs.ket_qua != 'thanh_cong').sum()
    he_thong = (ket_qua['tong'] + n_ko * BASELINE) / len(reqs)
    print(f"Cả hệ thống/yêu cầu (cộng {n_ko} ca nhân viên làm thay): {he_thong:,.0f} đ = x{he_thong / BASELINE:.2f}")
    return goc


def nhiem_vu_b(runs, reqs, goc):
    print('\n== B1 độ nhạy [simulated] ==')
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương tăng 25%': dict(luong_phut=2500),
        'Tối đa 2 lần chạy': dict(max_lan_chay=2),
        'Chỉ 1 lần chạy': dict(max_lan_chay=1),
    }
    for ten, kw in kich_ban.items():
        c = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:25s} {c:8,.0f} {(c / goc - 1) * 100:+6.1f}%')
    c = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'B2 token x2 + xem lại x2: {c:,.0f} {(c / goc - 1) * 100:+.1f}%')

    print('\n== B3 giới hạn chạy [simulated] ==')
    for k in (1, 2, 3):
        m = mo_hinh(runs, reqs, max_lan_chay=k)
        ko = len(reqs) - m['thanh_cong']
        print(f"k={k}: tổng trợ lý={m['tong']:,.0f} không thành công={ko} "
              f"cả hệ thống={m['tong'] + ko * BASELINE:,.0f} cps={m['cps']:,.0f}")

    print('\n== B4 xem lại 100% noi_dia+hang_nang [simulated] ==')
    sub = reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])]
    r_sub = runs[runs.request_id.isin(sub.request_id)]
    n_xem = r_sub[r_sub.status == 'ok'].request_id.nunique()
    ca_ll = sub[sub.ket_qua == 'lam_lai']
    tt = (r_sub.tokens_in / 1000 * GIA_VAO + r_sub.tokens_out / 1000 * GIA_RA + r_sub.tool_calls * GIA_TOOL).sum()
    v = (sub.ket_qua == 'thanh_cong').sum()
    print(f'{len(sub)} yêu cầu; có ≥1 lần ok={n_xem}; ca lam_lai={len(ca_ll)}; token+tool={tt:,.0f}; thành công={v}')
    for phut in (9, ca_ll.phut_lam_lai_simulated.mean()):
        tong = n_xem * 5 * LUONG_PHUT + len(ca_ll) * phut * LUONG_PHUT + tt
        # hoà vốn: số phút xem lại để cps = BASELINE
        hv = (BASELINE * v - tt - len(ca_ll) * phut * LUONG_PHUT) / (n_xem * LUONG_PHUT)
        print(f'làm lại {phut:.1f} phút/ca → {tong / v:,.0f} đ = x{tong / v / BASELINE:.2f}; hoà vốn xem lại ≤ {hv:.1f} phút')


def nhiem_vu_d(reqs):
    print('\n== D1 cỡ mẫu ==')
    n5 = co_mau(0.70, 0.75)
    print(f'a) theo yêu cầu: {n5} mỗi nhóm')
    de = 1 + 74 * ICC
    print(f'b) m=75: DE={de:.2f}, n={math.ceil(n5 * de)} mỗi nhóm → {math.ceil(n5 * de / 75)} người/nhóm (cần 2 nhóm; có 40 người)')
    print(f'c) 20 NV/nhóm: tối đa {20 / ICC:.0f} < {n5}')
    print(f'd) 6 depot/nhóm: tối đa {6 / ICC:.0f}')
    n6 = co_mau(0.70, 0.76)
    m_ = math.ceil(n6 * (1 - ICC) / (20 - n6 * ICC))
    print(f'e) MDE 6 điểm: n={n6}; m ≥ {m_} yêu cầu/người; DE={1 + (m_ - 1) * ICC:.2f}')
    from statsmodels.stats.power import NormalIndPower
    from statsmodels.stats.proportion import proportion_effectsize
    pw = NormalIndPower().power(proportion_effectsize(0.75, 0.70), nobs1=n6, alpha=0.05, ratio=1)
    print(f'power nếu tác động thật chỉ 5 điểm với n={n6}: {pw:.2f}')

    sub = reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])]
    print(f"\nmở lại 7 ngày: toàn mẫu {reqs.mo_lai_trong_7_ngay.mean():.2%}; "
          f"phạm vi {sub.mo_lai_trong_7_ngay.mean():.2%}; làm lại trong phạm vi {(sub.ket_qua == 'lam_lai').mean():.2%}")


def nhiem_vu_e(reqs):
    print('\n== E1 chỉ số ==')
    chinh = ((reqs.dong_trong_24h == 1) & (reqs.mo_lai_trong_7_ngay == 0))
    xem = reqs[reqs.duoc_xem_lai == 1]
    bo_qua = xem.quyet_dinh_xem_lai.isin(['sua', 'bo'])
    print(f'chính = {chinh.mean():.2%} ({chinh.sum()}/{len(reqs)})')
    print(f'dùng (bỏ qua gợi ý) = {bo_qua.mean():.2%} ({bo_qua.sum()}/{len(xem)})')
    print(f'an toàn (mở lại 7 ngày) = {reqs.mo_lai_trong_7_ngay.mean():.2%} ({reqs.mo_lai_trong_7_ngay.sum()}/{len(reqs)})')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    goc = nhiem_vu_a(runs, reqs)
    nhiem_vu_b(runs, reqs, goc)
    nhiem_vu_d(reqs)
    nhiem_vu_e(reqs)
