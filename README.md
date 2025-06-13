
# didactic-train

## Deskripsi Proyek

**didactic-train** adalah proyek Python yang dirancang untuk analisis data, perhitungan statistik, pengelolaan memori, serta seleksi dan generasi output berdasarkan berbagai dimensi kognitif dan statistik. Proyek ini menyatukan beberapa modul yang dapat digunakan untuk kebutuhan riset, pengembangan AI, dan otomasi analitik.

## Fitur Utama

- Analisis data berbasis dimensi psikologis dan statistik
- Perhitungan entropy (kompleksitas/ketidakpastian) pada teks
- Estimasi tingkat abstraksi dan kedalaman kognitif
- Pengelolaan memori data sementara
- Seleksi data otomatis sesuai kriteria tertentu
- Generasi output/informasi berbasis hasil analisis
- Contoh penggunaan dan konfigurasi mudah

## Struktur Direktori

```
didactic-train/
├── AB-Testing-Results/
├── DAnalyzer.py
├── ECalculator.py
├── HMemory.py
├── OGenerator.py
├── RSelector.py
├── UAnalyszer.py
├── config.json
├── examples.py
├── main.py
├── requirements.txt
├── setup.py
└── README.md
```

---

## Penjelasan Kode Per File

### 1. main.py

File utama aplikasi. Menjalankan alur utama, mengatur input/output, membaca konfigurasi, dan mengorkestrasi pemanggilan modul-modul lain.

---

### 2. DAnalyzer.py

Kelas `DimensionAnalyzer` digunakan untuk menganalisis dan menerapkan keterbatasan berdasarkan dua dimensi psikologis: gaya kognitif (`cognitive_style`) dan gaya pemrosesan (`processing_style`).  
Fitur utamanya:
- Menentukan aspek-aspek yang menjadi keterbatasan dari kombinasi gaya.
- Memberikan deskripsi keterbatasan pada output.
- Mensimulasikan pengaruh keterbatasan pada teks keluaran AI.

---

### 3. ECalculator.py

File ini berisi kelas `EntropyCalculator` dan sub-kelas `PFTFusion` yang berfokus pada perhitungan entropi (ukuran ketidakpastian atau kompleksitas) dari teks, serta estimator lanjutan seperti kedalaman kognitif dan tingkat abstraksi. Terdapat juga fitur integrasi "fusion" untuk penggabungan nilai berbasis meta-entropy.

**Penjelasan fitur utama:**

- **EntropyCalculator**
  - `calculate_text_entropy(text)`: Menghitung entropy Shannon dari teks input untuk mengukur keragaman karakter.
  - `normalize_entropy(entropy, max_possible=8)`: Mengubah nilai entropy ke skala 0–1 agar mudah dibandingkan atau divisualisasikan.
  - `get_entropy_level(normalized_entropy)`: Mengkategorikan entropy menjadi "low", "medium", atau "high" untuk interpretasi sederhana.

- **PFTFusion (sub-kelas)**
  - Menyimpan histori entropy dan menghitung meta-entropy (entropy dari distribusi nilai entropy sebelumnya).
  - `fuse(a, b)`: Melakukan penggabungan dua nilai dengan mempertimbangkan meta-entropy dan parameter temperatur.
  - `dynamic_threshold()`: Menghasilkan threshold adaptif berdasarkan rata-rata bergerak dari histori entropy.

- **Advanced Complexity Estimators**
  - `estimate_cognitive_depth(text)`: Estimasi kedalaman kognitif berdasarkan kepadatan kata kunci kompleksitas seperti “mengapa”, “analisis”, “strategi”.
  - `detect_abstraction_level(text)`: Mengukur tingkat abstraksi teks berdasarkan indikator linguistik abstrak (“konsep”, “prinsipnya”) dan konkret (“contoh”, “langkah”).

Modul ini memungkinkan analisis tingkat lanjut terkait kompleksitas, kedalaman, dan abstraksi sebuah teks, serta mendukung proses pengambilan keputusan yang lebih adaptif dan informatif.

---

### 4. HMemory.py

Pengelolaan memori atau cache data sementara untuk efisiensi proses analisis, terutama saat menangani data besar atau proses berulang.

---

### 5. OGenerator.py

Penghasil output atau data baru berdasarkan hasil analisis. Output bisa berupa laporan, data terolah, atau format lain sesuai kebutuhan pengguna.

---

### 6. RSelector.py

Pemilihan subset data berdasarkan kriteria tertentu. Penting untuk filtering atau segmentasi data sebelum analisis lebih lanjut.

---

### 7. UAnalyszer.py

Modul utilitas untuk analisis lanjutan, melengkapi fungsi yang tidak ada di DAnalyzer.py namun tetap mendukung proses utama.

---

### 8. config.json

File konfigurasi berisi parameter, path, dan pengaturan aplikasi. Dapat disesuaikan sesuai kebutuhan pengguna.

---

### 9. examples.py

Contoh penggunaan setiap modul agar pengguna baru mudah memahami cara kerja dan integrasinya.

---

### 10. requirements.txt

Daftar dependensi Python. Instalasi dengan:
```bash
pip install -r requirements.txt
```

---

### 11. setup.py

Skrip untuk instalasi dan distribusi sebagai package Python.

---

## Cara Instalasi & Penggunaan

1. **Klon repositori:**
    ```bash
    git clone https://github.com/Redazn/didactic-train.git
    cd didactic-train
    ```
2. **Instal dependensi:**
    ```bash
    pip install -r requirements.txt
    ```
3. **Jalankan aplikasi:**
    ```bash
    python main.py
    ```

---

## Kontribusi

Kontribusi sangat terbuka!  
Silakan fork, lakukan perubahan, dan buat pull request untuk penambahan fitur atau perbaikan bug. Pastikan kode telah diuji sebelum dikirim.

---

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).

---

