# 📌 ANN Benchmark: Annoy vs FAISS vs HNSW

## 🚀 Deskripsi Project

Project ini membandingkan tiga metode Approximate Nearest Neighbor (ANN) untuk sistem pencarian/rekomendasi berbasis vector embedding:

- Annoy (Tree-based ANN)
- FAISS (Exact & optimized search)
- HNSW (Graph-based ANN)

Tujuan utama eksperimen ini adalah memahami trade-off antara **kecepatan, akurasi, dan skalabilitas**.

---

## 📂 Dataset

Dataset yang digunakan berupa vector embedding:

- `xb` → database vector
- `xq` → query vector

Setiap data direpresentasikan dalam ruang berdimensi tinggi (contoh: 128 dimensi).

---

## ⚙️ Metode yang Digunakan

### 1. FAISS (IndexFlatL2)

FAISS digunakan sebagai **ground truth (exact nearest neighbor search)**.

- Tidak menggunakan approximation
- Hasil paling akurat
- Digunakan untuk menghitung Recall@K

---

### 2. Annoy

Annoy menggunakan struktur **random projection trees**.

- Cocok untuk sistem ringan
- Cepat dalam query
- Mengorbankan sedikit akurasi

---

### 3. HNSW (Hierarchical Navigable Small World)

HNSW menggunakan struktur **graph-based navigation**.

- Sangat efisien untuk dataset besar
- Trade-off terbaik antara speed dan accuracy
- Banyak digunakan di production system

---

## 📊 Evaluasi

Evaluasi dilakukan menggunakan:

### ⏱ 1. Query Time
Waktu yang dibutuhkan untuk mencari K nearest neighbors.

### 🎯 2. Recall@K

Mengukur seberapa banyak hasil ANN yang sesuai dengan ground truth FAISS:

```math
Recall@K = |I_{ANN} ∩ I_{FAISS}| / K
```

## 📈 Hasil Eksperimen

Hasil eksperimen perbandingan Annoy, FAISS, dan HNSW ditunjukkan pada tabel berikut:

| Method       | Build Time (sec) | Query Time (sec) | Recall@K |
|--------------|------------------|------------------|----------|
| Annoy        | 1.099401         | 0.000000         | 0.95     |
| FAISS (Flat) | 0.011693         | 0.003011         | 1.00     |
| HNSW         | 4.518057         | 0.000000         | 1.00     |

---

## 🧠 Insight Hasil

- **FAISS (Flat)** memberikan hasil paling akurat (Recall@K = 1.00) dengan waktu build yang paling cepat karena menggunakan optimasi brute-force yang sangat efisien.
- **HNSW** memiliki waktu build paling lama, tetapi tetap menghasilkan recall sempurna dan sangat efisien dalam pencarian berbasis graph.
- **Annoy** memiliki waktu build yang cukup cepat dan performa query yang ringan, dengan sedikit penurunan pada recall dibanding metode lainnya.

---

## 📌 Kesimpulan

Dari hasil eksperimen, dapat disimpulkan bahwa setiap metode memiliki keunggulan masing-masing:

- 🎯 **FAISS (Flat)** → terbaik untuk akurasi (exact search)
- ⚡ **HNSW** → terbaik untuk kombinasi scalability dan akurasi
- 🪶 **Annoy** → ringan dan cepat, cocok untuk sistem sederhana

Tidak ada satu metode yang secara mutlak terbaik, karena pemilihan algoritma bergantung pada kebutuhan sistem:

- Jika mengutamakan akurasi → FAISS  
- Jika mengutamakan skala besar + performa → HNSW  
- Jika mengutamakan kesederhanaan → Annoy  