# didactic-train


---


<p align="center">
  <img src="https://raw.githubusercontent.com/Redazn/didactic-train/main/logo.png" width="120" alt="didactic-train Logo" />
</p>

<p align="center">
  <a href="https://github.com/Redazn/didactic-train/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/Redazn/didactic-train/python-app.yml?branch=main&logo=github&style=flat-square" alt="Build Status">
  </a>
  <a href="https://github.com/Redazn/didactic-train/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/Redazn/didactic-train?style=flat-square" alt="License">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/python-3.8%2B-blue?logo=python&style=flat-square" alt="Python Version">
  </a>
  <a href="https://github.com/Redazn/didactic-train/commits/main">
    <img src="https://img.shields.io/github/last-commit/Redazn/didactic-train?style=flat-square" alt="Last Commit">
  </a>
  <a href="https://github.com/Redazn/didactic-train/stargazers">
    <img src="https://img.shields.io/github/stars/Redazn/didactic-train?style=flat-square" alt="Stars">
  </a>
</p>

---

## 📦 Deskripsi

**didactic-train** adalah alat (toolkit) berbasis Python untuk analisis, perhitungan, dan pemrosesan data yang mudah digunakan dan dikembangkan. Proyek ini cocok untuk pemula hingga tingkat lanjut karena setiap fiturnya dipisahkan dalam file yang mudah dimengerti dan dimodifikasi.

---

## ✨ Fitur

- Mudah dikembangkan (modular)
- Pengaturan fleksibel lewat `config.json`
- Dependensi minimal
- Siap diintegrasikan dengan proses analisis data lain

---

## 🗂️ Struktur Direktori

```
.
├── DAnalyzer.py
├── ECalculator.py
├── OGenerator.py
├── RSelector.py
├── config.json
├── main.py
├── requirements.txt
├── setup.py
├── LICENSE
├── README.md
├── logo.png
└── examples.py
```

---

## 🚀 Instalasi

1. **Clone repo:**
    ```bash
    git clone https://github.com/Redazn/didactic-train.git
    cd didactic-train
    ```
2. **Install dependensi:**
    ```bash
    pip install -r requirements.txt
    ```

---

## 💡 Penggunaan Dasar

Jalankan aplikasi utama:
```bash
python main.py
```
Anda dapat mengubah proses dan pengaturan lewat file `config.json`.

---

## ⚙️ Konfigurasi (`config.json`)

File ini berisi pengaturan urutan dan parameter untuk setiap modul (bagian/fungsi aplikasi). Contoh:

```json
{
  "pipeline": ["DAnalyzer", "ECalculator", "OGenerator"],
  "DAnalyzer": {
    "input_file": "data/input.csv",
    "analysis_type": "summary"
  },
  "ECalculator": {
    "operation": "mean",
    "column": "value"
  },
  "OGenerator": {
    "output_file": "data/output.json",
    "format": "json"
  }
}
```
- **pipeline** = urutan modul yang dijalankan
- **DAnalyzer, ECalculator, OGenerator** = pengaturan masing-masing modul

---

## 🧑‍💻 Contoh Penggunaan Lengkap: `examples.py`

File ini sangat cocok untuk pemula karena:

- Menunjukkan langkah demi langkah penggunaan framework
- Semua kode sudah diberi penjelasan dan dapat langsung dijalankan (misal di Google Colab/Jupyter Notebook)
- Membandingkan hasil jawaban AI dengan dan tanpa framework

### Isi File [examples.py](https://github.com/Redazn/didactic-train/blob/main/examples.py):


---

### Cara Menjalankan Contoh (`examples.py`):

1. **Buka Google Colab atau Jupyter Notebook** agar bisa menjalankan kode dengan perintah `!` dan `%`.
2. **Masukkan API Key Gemini** pada bagian `GEMINI_API_KEY = "!!!!!!!!"`.
3. **Jalankan satu per satu** kode dalam contoh, atau jalankan seluruh script.
4. **Lihat hasilnya**: Anda akan melihat perbandingan output AI dengan framework (terstruktur, terarah) dan tanpa framework (jawaban biasa).

---

## 🧩 Kontribusi

Kontribusi sangat terbuka!  
Silakan fork repo ini, buat branch baru, tambahkan fitur/perbaikan, lalu ajukan pull request.

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah [LICENSE](https://github.com/Redazn/didactic-train/blob/main/LICENSE).

---

## 🙏 Terima Kasih

Terima kasih telah menggunakan **didactic-train**!  
Jangan lupa kasih ⭐ jika bermanfaat!

---

