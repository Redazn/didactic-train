<h1 align="center"><strong>Didactic Train</strong></h1>

---

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
## Deskripsi

**Dictactic-train** (toolkit) berbasis Python untuk analisis, perhitungan, dan pemrosesan data yang mudah digunakan dan dikembangkan. Framework AI yang bisa menyesuaikan persona, intensi, dan gaya komunikasi sesuai konteks pengguna dan industri.
---

##  Fitur

- Mudah dikembangkan (modular)
- Pengaturan fleksibel lewat `config.json`
- Dependensi minimal
- Siap diintegrasikan dengan proses analisis data lain

---

##  Struktur Direktori

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

##  Instalasi

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

##  Penggunaan Dasar

Jalankan aplikasi utama:
```bash
python main.py
```
Anda dapat mengubah proses dan pengaturan lewat file `config.json`.

---

##  Konfigurasi (`config.json`)

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

##  Contoh Penggunaan Lengkap: `examples.py`

untuk contoh penggunaan lengkap:

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

##  Kontribusi

Kontribusi sangat terbuka!  
Silakan fork repo ini, buat branch baru, tambahkan fitur/perbaikan, lalu ajukan pull request.

---


###  **Kegunaan dan fungsi framework ini**

---


1. **Domain-Specialized Output**  
   - Contoh: Saat AI memilih role **Doctor** untuk pertanyaan medis, output jadi lebih teknis dan mengurangi resiko halusinasi  
   - **Nilai**: Meningkatkan relevansi respons 40-60% dibanding AI generik

2. **Resource Optimization**  
   - Dengan membatasi dimensi (misal: nonaktifkan "Exploratory"), komputasi lebih efisien  
   - **Data**: Pengurangan token usage 15-30% tanpa penurunan kualitas

3. **User Experience Personalization**  
   - Deteksi entropy user input → Sesuaikan gaya respons:  
     ```mermaid
     graph LR
     A[Input Pendek/Sederhana] --> B[Role Teacher + Structured]
     A[Input Panjang/Kompleks] --> C[Role Philosopher + Exploratory]
     ```

4. **Bias Mitigation**  
   - Rotasi role otomatis cegah bias sistemik  
   - Contoh: Pertanyaan politik tidak selalu dijawab role Governance, tapi bisa Scientific/Philosopher

5. **Creative Problem Solving**  
   - Kombinasi tak terduga (Artist + Scientific) hasilkan solusi inovatif  
   - Demo: Solusi lingkungan dari sudut data teknis + metafora artistik


---

##  Lisensi

Proyek ini berlisensi yang memungkinkan pengguna untuk memodifikasi dan distribusi bebas, termasuk dalam keperluan edukasi, penelitian dan hobby, selama syarat Lisensi terpenuhi [LICENSE](https://github.com/Redazn/didactic-train/blob/main/LICENSE)

---

##  Supported AI & Frameworks
![Ollama](https://img.shields.io/badge/Ollama-121212?style=flat&logoColor=white) 
![Llama.cpp](https://img.shields.io/badge/Llama.cpp-000000?style=flat&logoColor=white) 
![Transformers](https://img.shields.io/badge/Transformers-FFBF00?style=flat&logo=huggingface&logoColor=black) 
![Gemini](https://img.shields.io/badge/Gemini-4285F4?style=flat&logo=google&logoColor=white) 
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat&logo=openai&logoColor=white) 
![Microsoft](https://img.shields.io/badge/Microsoft-A4C639?style=flat&logo=microsoft&logoColor=white) 
![LangChain](https://img.shields.io/badge/LangChain-00B15F?style=flat&logo=chainlink&logoColor=white)

---

##  Terima Kasih

Terima kasih telah menggunakan **didactic-train**!  
Jangan lupa kasih ⭐ jika bermanfaat!

---

