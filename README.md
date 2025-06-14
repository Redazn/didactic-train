
# SYA(Sedyatama) - 
**'Adaptive Multi-role switching'**

---

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

File ini berisi kelas utama `DimensionAnalyzer` yang berfungsi untuk menganalisis dan menerapkan keterbatasan (constraints) pada output berdasarkan dua dimensi psikologis: gaya kognitif (`cognitive_style`) dan gaya pemrosesan (`processing_style`).  
Kelas ini dapat digunakan untuk menyimulasikan bagaimana jenis gaya berpikir tertentu mempengaruhi hasil keluaran AI.

- **`__init__`**: Konstruktor yang menginisialisasi dua atribut gaya kognitif dan pemrosesan.
- **`limitations` (property)**: Menghasilkan daftar keterbatasan berdasarkan kombinasi kedua gaya.
- **`get_constraint_description()`**: Menyusun deskripsi ringkas terkait keterbatasan berdasarkan dimensi.
- **`apply_constraints(output_text)`**: Mensimulasikan penerapan keterbatasan pada output teks, misalnya mengganti frase sesuai gaya berpikir yang dipilih.

Contoh penggunaan:
```python
analyzer = DimensionAnalyzer("Analytical", "Structured")
print(analyzer.get_constraint_description())
print(analyzer.apply_constraints("saya merasa data menunjukkan tren positif"))
```


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

Contoh penggunaan:
```python
entropy = EntropyCalculator.calculate_text_entropy("Contoh teks untuk analisis")
normalized = EntropyCalculator.normalize_entropy(entropy)
print("Entropy Level:", EntropyCalculator.get_entropy_level(normalized))

fusion = EntropyCalculator.PFTFusion(temperature=0.5, window_size=10)
fused_value = fusion.fuse(0.8, 0.3)
print("Fused Value:", fused_value)
```


---

### 4. HMemory.py

File ini berisi kelas `PFTCognitiveMemory` yang disusun untuk mensimulasikan proses memori kognitif pada sistem AI, dengan penggabungan informasi dari memori jangka pendek (STM) dan jangka panjang (LTM).

**Fitur utama:**

- **Struktur Memori**
  - `short_term`: Menyimpan konteks atau memori jangka pendek.
  - `long_term`: Menyimpan pengalaman atau memori jangka panjang.
  - `theta_params`: Parameter bobot untuk fusi memori (misal, perbandingan antara STM dan LTM).
  - `phi_threshold`: Ambang nilai untuk integrasi fusi.

- **Metode Utama**
  - `store_experience(key, experience)`: Menyimpan pengalaman baru ke dalam LTM.
  - `activate_context(context)`: Mengaktifkan atau mengisi memori jangka pendek dengan konteks saat ini.
  - `pft_fusion_operator()`: Melakukan fusi antara STM dan LTM:
    - Mencari pengalaman paling relevan dari LTM.
    - Menghitung keselarasan semantik antara STM dan pengalaman LTM menggunakan cosine similarity.
    - Menghitung kekuatan interaksi berdasarkan cosine similarity antar vektor state.
    - Menghitung bobot fusi berdasarkan parameter dan skor interaksi.
    - Menghasilkan state baru dengan kombinasi dari STM, LTM, dan perhitungan interaksi semantik.
    - Mengembalikan dictionary berisi state yang telah difusikan, makna koheren, bobot fusi, dan sumber.
  - `calculate_emergence_index(fused_state)`: Menghitung indeks emergensi berdasarkan perbandingan performa state; jika signifikan, hasil fusi disimpan sebagai pengalaman baru di LTM.
  - `find_most_relevant()`: Mencari pengalaman LTM yang paling sesuai dengan konteks STM berdasarkan keselarasan semantik.
  - `calculate_semantic_alignment(meaning_A, meaning_B)`: Menghitung keselarasan antara dua makna dengan cosine similarity dari vektor embedding.
  - `semantic_interaction(state_A, state_B)`: Menghasilkan state baru melalui interaksi vektor (operasi perkalian dan normalisasi).
  - `coherent_meaning(meaning_A, meaning_B)`: Menggabungkan dua input string menjadi satu makna koheren.
  - `get_embedding(text)`: Menghasilkan embedding vektor untuk teks (contoh dummy, implementasi bisa disesuaikan).
  - `evaluate_performance(state)`: Mengevaluasi performa suatu state, misalnya dengan menghitung norm vektor state.

Contoh penggunaan:
```python
memory = PFTCognitiveMemory()

# Set konteks memori jangka pendek
memory.activate_context({
    'state': [0.2, 0.4, 0.6],
    'meaning': "analisis data kontemporer"
})

# Simpan pengalaman di LTM
memory.store_experience("experience_1", {
    'state': [0.1, 0.3, 0.5],
    'meaning': "data historis",
    'performance': 1.2
})

# Lakukan fusi
fused_result = memory.pft_fusion_operator()
print("Fused Result:", fused_result)
```


---

### 5. OGenerator.py

Penghasil output atau data baru berdasarkan hasil analisis. Output bisa berupa laporan, data terolah, atau format lain sesuai kebutuhan pengguna.

---

### 6. RSelector.py

File ini berisi kelas `RoleSelector` yang bertujuan untuk memilih role dan kombinasi dimensi kognitif berdasarkan nilai entropy yang dihasilkan dari analisis. Proses seleksi menggunakan konfigurasi yang disediakan dalam bentuk dictionary, sehingga pemilihan role dan dimensi bersifat adaptif terhadap tingkat entropy yang diamati.

- **Fitur Utama:**  
  Menyediakan mekanisme seleksi role dan kombinasi dimensi kognitif melalui kelas `RoleSelector`, yang:
  - Memilih role berdasarkan tingkat entropy menggunakan konfigurasi bobot dari file konfigurasi.
  - Memilih kombinasi dimensi kognitif (gaya kognitif dan gaya pemrosesan) secara acak sesuai bobot yang ditetapkan untuk setiap level entropy menggunakan metode probabilistik.


**Contoh Pemakaian:**

Misalnya, jika konfigurasi `config` berbentuk seperti berikut:

```python
config = {
    'roles': ['Leader', 'Support', 'Innovator'],
    'role_weights': {
        'low': [0.7, 0.2, 0.1],
        'medium': [0.3, 0.5, 0.2],
        'high': [0.1, 0.3, 0.6]
    },
    'dimension_weights': {
        'low': {
            'Analytical': 0.8,
            'Emotive': 0.2,
            'Structured': 0.9,
            'Exploratory': 0.1
        },
        'medium': {
            'Analytical': 0.5,
            'Emotive': 0.5,
            'Structured': 0.5,
            'Exploratory': 0.5
        },
        'high': {
            'Analytical': 0.2,
            'Emotive': 0.8,
            'Structured': 0.1,
            'Exploratory': 0.9
        }
    }
}
```

Anda dapat menggunakan kelas `RoleSelector` sebagai berikut:

```python
selector = RoleSelector(config)

# Misalnya, jika level entropy 'medium':
selected_role = selector.select_role('medium')
selected_dimensions = selector.select_dimensions('medium')

print("Role terpilih:", selected_role)
print("Dimensi terpilih:", selected_dimensions)
```

Pada contoh di atas, fungsi `select_role` akan mengembalikan role dari daftar role yang dipilih secara acak berdasarkan bobot pada level 'medium', dan `select_dimensions` akan mengembalikan kombinasi dimensi kognitif sesuai dengan bobot yang ditentukan untuk level tersebut.


---

### 7. UAnalyszer.py

Module ini menyediakan metode untuk menganalisis ketidakpastian dalam sebuah teks secara sederhana. Metode ini mengukur tingkat keragaman kata yang ada dalam teks, dengan membandingkan jumlah kata unik dengan total kata. Hasil perhitungan ini memberikan gambaran tentang "ketidakpastian" dalam teks, di mana nilai yang lebih tinggi menunjukkan variasi kata yang lebih banyak. Selain itu, modul ini menyediakan

- **Fitur Utama:**

  - **`analyze_uncertainty(text)`:**  
  Menganalisis teks dengan cara mengekstrak kata-kata (token) menggunakan regular expression, kemudian menghitung rasio antara jumlah kata unik dan total kata. Jika tidak ada token yang ditemukan, maka fungsi mengembalikan nilai 0.0.
  
  - **`normalize_uncertainty(uncertainty)`:**  
  Menormalkan nilai ketidakpastian yang diperoleh sehingga selalu berada dalam rentang 0 hingga 1, menggunakan fungsi pembatas.

**Contoh Penggunaan:**

```python
from UAnalyszer import Uncertainty
```

Dengan contoh di atas, Anda dapat mengukur sejauh mana suatu teks memiliki variasi kata dan memastikan nilai tersebut berada pada rentang yang konsisten untuk proses analisis selanjutnya.


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

