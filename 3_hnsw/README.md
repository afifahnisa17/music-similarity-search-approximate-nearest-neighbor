# 🧠 Sistem Rekomendasi Musik dengan HNSW

## 📌 Gambaran Umum

Proyek ini mengimplementasikan sistem rekomendasi musik menggunakan **HNSW (Hierarchical Navigable Small World graphs)** untuk mencari lagu yang memiliki kemiripan berdasarkan fitur audio.

Pendekatan yang digunakan adalah **content-based filtering**, di mana setiap lagu direpresentasikan sebagai vektor fitur audio tanpa menggunakan rating atau interaksi pengguna.

---

## ⚙️ Cara Kerja Sistem

Setiap lagu direpresentasikan sebagai vektor numerik yang terdiri dari fitur audio seperti:

- acousticness  
- danceability  
- energy  
- tempo  
- valence  
- instrumentalness  
- loudness  

HNSW membangun struktur **graph bertingkat (multi-layer graph)** untuk melakukan pencarian approximate nearest neighbor secara efisien.

---

## 🔍 Inti Sistem

HNSW bekerja dengan cara:

- Setiap lagu direpresentasikan sebagai node dalam graph
- Node terhubung dengan tetangga terdekatnya
- Pencarian dilakukan dengan navigasi dari node awal menuju kandidat terdekat
- Tidak perlu menghitung jarak ke seluruh dataset

---

## 🚀 Alur Proses

1. Memuat dataset fitur audio (`features.npy`) dan metadata (`meta.csv`)
2. Inisialisasi index HNSW
3. Menambahkan seluruh vektor ke graph
4. Melakukan query berdasarkan satu lagu
5. Mengambil K nearest neighbors
6. (Opsional) melakukan filtering berdasarkan genre
7. Menampilkan hasil rekomendasi

---

## ⚙️ Parameter Penting

### 🔹 M (Connectivity)
Mengatur jumlah koneksi per node dalam graph.

- M kecil → lebih cepat, tapi kualitas turun  
- M besar → lebih akurat, tapi lebih berat  

---

### 🔹 efConstruction
Mengontrol kualitas graph saat proses build.

- Semakin besar → graph lebih optimal  
- Tapi waktu build lebih lama  

---

### 🔹 efSearch
Mengontrol kualitas pencarian saat query.

- kecil → lebih cepat  
- besar → lebih akurat  

---

## ⚖️ Parameter K (Jumlah Neighbor)

Parameter **K** menentukan jumlah kandidat hasil retrieval.

- K kecil → hasil lebih ketat, tapi berisiko kurang kandidat  
- K besar → lebih banyak kandidat untuk filtering dan ranking  

Dalam eksperimen ini:
- K = 20 digunakan untuk menjaga keseimbangan antara kecepatan dan coverage

---

## 🎧 Filtering (Genre-Based Constraint)

Selain pencarian berbasis kemiripan vektor, sistem juga dapat menerapkan **filtering berdasarkan genre**.

### 📌 Tanpa Filtering
- Hasil adalah nearest neighbors berdasarkan similarity saja
- Lebih murni berbasis embedding space

### 📌 Dengan Filtering
- Hasil hanya menampilkan lagu dengan genre yang sama
- Jika kandidat tidak cukup, sistem fallback ke hasil terdekat

---

## 📊 Insight Eksperimen

Hasil eksperimen menunjukkan bahwa:

- HNSW mampu menghasilkan rekomendasi dengan latensi sangat rendah
- Hasil rekomendasi tidak selalu selaras dengan genre karena sistem berbasis embedding similarity
- Setelah filtering genre, jumlah hasil dapat berkurang signifikan karena tidak semua nearest neighbors memenuhi constraint
- Ini menunjukkan perbedaan antara **vector similarity** vs **attribute constraint filtering**

---


## 🧠 Teknologi yang Digunakan

- Python  
- NumPy  
- Pandas  
- hnswlib  
- scikit-learn (baseline comparison)  

---

## 📌 Catatan

Eksperimen ini merupakan bagian dari perbandingan sistem:
- Annoy 
- FAISS 
- HNSW 

untuk menganalisis trade-off antara kecepatan, akurasi, dan fleksibilitas dalam sistem rekomendasi berbasis embedding.