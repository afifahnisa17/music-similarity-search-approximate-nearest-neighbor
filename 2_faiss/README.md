# ⚡ Sistem Rekomendasi Musik dengan FAISS

## 📌 Gambaran Umum

Proyek ini mengimplementasikan sistem rekomendasi musik menggunakan **FAISS (Facebook AI Similarity Search)** untuk mencari lagu yang memiliki kemiripan berdasarkan fitur audio.

Pendekatan yang digunakan adalah **content-based filtering**, di mana setiap lagu direpresentasikan sebagai vektor fitur audio tanpa menggunakan rating atau interaksi pengguna.

---

## ⚙️ Cara Kerja Sistem

Setiap lagu diubah menjadi representasi vektor yang terdiri dari fitur audio seperti:

- acousticness  
- danceability  
- energy  
- tempo  
- valence  
- instrumentalness  
- loudness  

FAISS kemudian digunakan untuk melakukan pencarian **nearest neighbor** berdasarkan jarak dalam ruang vektor.

---

## 🔍 Inti Sistem

FAISS mencari lagu yang paling mirip berdasarkan kedekatan fitur audio.

Artinya:
- Lagu dengan karakteristik audio yang mirip akan berada dalam ruang vektor yang berdekatan
- Rekomendasi dapat mencerminkan kemiripan “vibe” musik
- Tidak bergantung pada genre atau label secara langsung

---

## 🚀 Alur Proses

1. Memuat dataset (fitur audio + metadata)
2. Membuat index FAISS (IndexFlatL2)
3. Melakukan query berdasarkan satu lagu
4. Mengambil K nearest neighbors
5. Menampilkan hasil rekomendasi (judul, artis, genre)

---

## ⚙️ Jenis Index yang Digunakan

### 🔹 IndexFlatL2 (Exact Search)
- Menghitung jarak ke seluruh data secara langsung
- Memberikan hasil paling akurat
- Cocok untuk dataset kecil hingga menengah

---

## ⚖️ Parameter K (Jumlah Neighbor)

Parameter **K** menentukan jumlah kandidat hasil yang diambil dari proses retrieval.

- K kecil → hasil lebih ketat tetapi berisiko kehilangan kandidat relevan  
- K besar → lebih banyak kandidat untuk seleksi atau filtering lanjutan  

Dalam implementasi ini:
- K = 20 digunakan untuk memastikan cakupan kandidat yang cukup sebelum ditampilkan sebagai top-N hasil

---

## ⚡ Performa

FAISS dikenal memiliki performa tinggi karena:

- Implementasi C++ yang sangat optimal  
- Menggunakan optimisasi low-level (SIMD)  
- Sangat cepat untuk pencarian vektor skala menengah hingga besar  

---

## 📊 Insight Eksperimen

Hasil eksperimen menunjukkan bahwa:

- FAISS menghasilkan rekomendasi yang konsisten berdasarkan kemiripan fitur audio
- Lagu dengan genre serupa (misalnya Movie soundtrack) cenderung mengelompok secara alami dalam ruang vektor
- Query tertentu dapat menghasilkan cluster genre dominan karena struktur data fitur

---


## 🧠 Teknologi yang Digunakan

- Python  
- NumPy  
- Pandas  
- FAISS  
- Matplotlib  

---

## 📁 Catatan

Implementasi ini digunakan sebagai bagian dari perbandingan dengan:
- Annoy  
- HNSW  

untuk menganalisis trade-off antara kecepatan, akurasi, dan skalabilitas pada sistem pencarian nearest neighbor.