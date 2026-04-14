# 🎧 Music Recommendation System menggunakan Approximate Nearest Neighbors (ANN)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://music-recommendation-faiss.streamlit.app/)

## 🚀 Ringkasan Proyek

Proyek ini membangun sistem rekomendasi musik berbasis **vector similarity search** menggunakan fitur audio dari Spotify.

Saya mengimplementasikan dan membandingkan beberapa algoritma **Approximate Nearest Neighbor (ANN)** untuk mencari lagu yang mirip secara efisien dalam skala data besar.

Fokus utama proyek ini adalah memahami trade-off antara:

- ⚡ Kecepatan query (latency)
- 🏗 Waktu pembuatan index (build time)
- 🎯 Akurasi hasil (Recall@K)

---

## 🎯 Permasalahan

Dengan dataset musik berskala besar (~232.000 lagu), kita ingin:

- Melakukan pencarian kemiripan lagu secara cepat di ruang vektor berdimensi tinggi  
- Membandingkan metode exact search vs approximate search  
- Mengoptimalkan keseimbangan antara kecepatan, akurasi, dan skalabilitas  

Masalah ini sangat relevan dengan sistem rekomendasi modern seperti Spotify dan YouTube Music.

---

## 📊 Dataset

Dataset yang digunakan:

🔗 https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db

### Deskripsi:
- ~232.000 track musik dari Spotify Web API  
- ~10.000 track per genre (26 genre)  
- Fitur audio meliputi:
  - danceability
  - energy
  - valence
  - tempo
  - acousticness
  - instrumentalness
  - dan lainnya

---

## ⚙️ Metode yang Digunakan

Proyek ini membandingkan tiga pendekatan ANN:

### 🟢 Annoy (Tree-based ANN)
- Menggunakan random projection tree
- Ringan dan cepat dalam proses build index
- Sedikit trade-off pada akurasi

### 🔵 FAISS (Exact / Flat Search)
- Brute-force nearest neighbor search
- Akurasi 100% (baseline exact search)
- Sangat cepat jika dioptimalkan (CPU/GPU)

### 🔴 HNSW (Graph-based ANN)
- Struktur graph navigable small world
- Sangat efisien untuk dataset besar
- Umum digunakan dalam sistem produksi

---

## 📦 Struktur Proyek
```
├── 0_data/
│ ├── raw/
│ │ └── spotify_features.csv
│ └── processed/
│   ├── features.npy
│   ├── meta.csv
│   └── spotify_features.ipynb
│
├── 1_annoy/
│ ├── annoy.ipynb
│ ├── annoy_filtered.ipynb
│ └── README.md
│
├── 2_faiss/
│ ├── faiss.ipynb
│ └── README.md
│
├── 3_hnsw/
│ ├── hnsw.ipynb
│ ├── hnsw_filtered.ipynb
│ └── README.md
│
├── 4_benchmark/
│ ├── comparison.ipynb
│ └── README.md
│
└── README.md
```

---

## 📈 Metrik Evaluasi

Evaluasi dilakukan menggunakan:

- 🎯 **Recall@K** → seberapa banyak neighbor asli yang berhasil ditemukan  
- ⚡ **Waktu Query** → latensi pencarian per request  
- 🏗 **Waktu Build Index** → waktu pembuatan struktur index  
- 💾 **Skalabilitas sistem**

---

## 📊 Hasil Perbandingan

| Metode       | Recall@K | Kecepatan Query | Waktu Build |
|--------------|----------|------------------|-------------|
| Annoy        | 0.95     | Cepat            | Sedang      |
| FAISS (Flat) | 1.00     | Sangat Cepat     | Sangat Cepat|
| HNSW         | 1.00     | Sangat Cepat     | Lambat      |

---

## 🧠 Insight Utama

- **FAISS (Flat)** memberikan akurasi sempurna, tetapi kurang scalable untuk data sangat besar
- **HNSW** memberikan keseimbangan terbaik antara kecepatan dan akurasi
- **Annoy** ringan dan cepat dibangun, tetapi sedikit kalah akurat pada data dense

➡️ Dalam skenario production, **HNSW adalah pilihan paling realistis** untuk sistem rekomendasi berskala besar.

---

## 🎧 Use Case

Sistem ini dapat dikembangkan untuk:

- Sistem rekomendasi musik (Spotify-like)
- Pembuatan playlist otomatis berdasarkan kemiripan
- Pencarian audio berbasis konten (content-based retrieval)
- Sistem rekomendasi real-time

---

## 🛠 Tech Stack

- Python
- NumPy
- Pandas
- Scikit-learn
- FAISS
- Annoy
- HNSWLib
- Jupyter Notebook

---

## 🚀 Pengembangan Selanjutnya

- Hybrid recommendation (content-based + collaborative filtering)
- Integrasi Spotify API untuk rekomendasi real-time
- Deployment menggunakan Streamlit / FastAPI
- Perbandingan dengan vector database (Pinecone / Weaviate)
- Benchmark GPU vs CPU untuk FAISS

---

## 🧠 Kesimpulan

Proyek ini menunjukkan bagaimana pendekatan ANN bekerja dalam sistem rekomendasi skala besar.

---