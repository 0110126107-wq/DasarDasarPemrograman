import pandas as pd
import streamlit as st


# 1. Fungsi buatan sendiri (untuk menghitung total, diskon, dan harga akhir)
def hitung_transaksi(harga, jumlah, is_member, metode_bayar):
    subtotal = harga * jumlah
    diskon = 0

    # Logika if/else untuk menentukan besaran diskon
    if is_member == "Member" and subtotal >= 100000:
        diskon = 0.15 * subtotal  # Diskon 15% untuk member belanja min. 100rb
    elif is_member == "Member" or subtotal >= 100000:
        diskon = 0.05 * subtotal  # Diskon 5% jika salah satu syarat terpenuhi
    else:
        diskon = 0  # Tidak dapat diskon

    # Tambahan potongan jika bayar pakai QRIS
    if metode_bayar == "QRIS":
        diskon += 5000

    # Mencegah total akhir menjadi minus
    total_akhir = max(0, subtotal - diskon)
    return subtotal, diskon, total_akhir


# Tampilan Antarmuka Streamlit
st.title("🛒 Aplikasi Kasir & Grafik Diskon")
st.write("Masukkan detail belanjaan di bawah ini:")

# 2. Empat (4) Widget Input Utama + 1 Metode Pembayaran
nama_barang = st.text_input("1. Nama Barang", value="Kopi Susu")
harga_satuan = st.number_input(
    "2. Harga Satuan (Rp)", min_value=0, value=25000, step=1000
)
jumlah_beli = st.number_input("3. Jumlah Beli", min_value=1, value=4, step=1)
status_member = st.radio("4. Status Pelanggan", ["Non-Member", "Member"])
metode = st.selectbox("Metode Pembayaran", ["Tunai", "QRIS", "Debit"])

# Tombol untuk memproses perhitungan
if st.button("Hitung Total"):
    # Memanggil fungsi buatan sendiri
    subtotal, total_diskon, total_bayar = hitung_transaksi(
        harga_satuan, jumlah_beli, status_member, metode
    )

    st.divider()
    st.subheader(f"Struk Pembelian: {nama_barang}")

    # 3. Output menggunakan st.metric
    col1, col2, col3 = st.columns(3)
    col1.metric("Subtotal", f"Rp {subtotal:,.0f}")
    col2.metric(
        "Total Diskon", f"Rp {total_diskon:,.0f}", delta=f"-Rp {total_diskon:,.0f}"
    )
    col3.metric("Total Bayar", f"Rp {total_bayar:,.0f}")

    # 4. Output Grafik Pengeluaran vs Diskon
    st.subheader("📊 Visualisasi Rincian Biaya")
    data_grafik = pd.DataFrame({
        "Kategori": ["Subtotal Awal", "Total Diskon", "Total Bayar Akhir"],
        "Nominal (Rp)": [subtotal, total_diskon, total_bayar],
    })

    # Menampilkan grafik batang
    st.bar_chart(data_grafik, x="Kategori", y="Nominal (Rp)", color="Kategori")
