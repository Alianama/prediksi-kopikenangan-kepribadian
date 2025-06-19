# Ngopi Yuk! - Rekomendasi Menu Kopi Kenangan Berdasarkan Kepribadian

Aplikasi ini adalah web app interaktif berbasis Streamlit yang merekomendasikan menu Kopi Kenangan paling cocok untukmu berdasarkan kepribadian dan preferensi pribadi. Aplikasi ini juga mengadopsi nuansa visual ala website Kopi Kenangan.

---

## ✨ Fitur Utama
- **Kuis Kepribadian:** User mengisi pertanyaan tentang kepribadian dan preferensi (dengan slider skala 1-5 dan pilihan ekonomi).
- **Rekomendasi Menu Otomatis:** Sistem merekomendasikan menu Kopi Kenangan yang paling sesuai dari dataset asli menu Kopi Kenangan.
- **Visualisasi Statistik:** Pie chart distribusi tipe menu.
- **Tampilan Modern:** UI mirip Kopi Kenangan, lengkap dengan logo dan warna khas.
- **Ekspor Dataset:** Dataset menu otomatis diekspor ke file CSV.

---

## 🧑‍💻 Cara Install & Menjalankan
1. **Clone repo & masuk ke folder project:**
   ```bash
   git clone <repo-anda>
   cd PrediksiKopiKesukaan
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Jalankan aplikasi:**
   ```bash
   streamlit run app.py
   ```
4. **Akses di browser:**
   Buka `http://localhost:8501`

---

## 📂 Struktur Data & Dataset
- **menu_kopi_kenangan.csv** berisi data asli menu Kopi Kenangan:
  - Nama Menu
  - Komposisi
  - Harga
  - Tipe (Kopi, Non-Kopi, Freezy, Oatside, Camilan, Paket)
  - Rasa Manis (Ya/Tidak)
  - Ada Susu (Ya/Tidak)
  - Ada Kopi (Ya/Tidak)
  - Ada Boba (Ya/Tidak)
  - Favorit (Ya/Tidak)

---

## 🤖 Algoritma & Cara Kerja
### 1. **Machine Learning: K-Nearest Neighbors (KNN)**
- Model KNN digunakan untuk mencari menu yang paling "mirip" dengan preferensi user.
- Fitur yang digunakan: Tipe, Rasa Manis, Ada Susu, Ada Kopi, Ada Boba, Favorit.
- Model dilatih setiap kali aplikasi dijalankan dengan data dari CSV.

### 2. **Mapping Kepribadian ke Fitur Menu**
- User mengisi kuis kepribadian (Tipe Kepribadian, Suka Manis, Aktif Malam, Suka Nongkrong, Pekerja Kreatif) dengan slider skala 1-5.
- Jawaban slider di-mapping ke fitur menu (Ya/Tidak) dengan aturan:
  - Nilai > 3 = "Ya"
  - Nilai ≤ 3 = "Tidak"
- Preferensi ekonomi user (Ekonomis, Standar, Premium) digunakan untuk memfilter menu berdasarkan harga.
- Hasil mapping digunakan sebagai input prediksi ke model KNN.

### 3. **Prediksi & Rekomendasi**
- Model KNN mencari menu terdekat dari preferensi user.
- Hanya menu dengan harga sesuai preferensi ekonomi yang dipertimbangkan.
- Hasil rekomendasi menampilkan nama menu, harga, dan komposisi.

---

## 📝 Contoh Penggunaan
1. Pilih tipe kepribadian dan atur slider preferensi sesuai diri Anda.
2. Pilih preferensi ekonomi (budget).
3. Klik "🎯 Rekomendasikan Menu!".
4. Lihat hasil rekomendasi menu Kopi Kenangan yang cocok untuk Anda.

---

## 📊 Visualisasi
- Pie chart distribusi tipe menu Kopi Kenangan dari dataset.

---

## 👨‍🎓 Pengembang
- Ali Purnama - Universitas Pelita Bangsa

---

## 📄 Lisensi
Aplikasi ini dibuat untuk tujuan edukasi dan non-komersial.

---

## 💡 Catatan
- Dataset menu dapat diperbarui dengan mengganti file `menu_kopi_kenangan.csv`.
- Mapping kepribadian ke fitur menu dapat dikembangkan lebih lanjut sesuai kebutuhan. 