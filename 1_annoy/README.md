# 🎵 Sistem Rekomendasi Musik dengan Annoy

## 📌 Gambaran Umum

Proyek ini mengimplementasikan sistem rekomendasi musik menggunakan **Annoy (Approximate Nearest Neighbors Oh Yeah)** untuk mencari lagu yang memiliki kemiripan berdasarkan karakteristik audio.

Pendekatan yang digunakan adalah **content-based filtering**, yaitu merekomendasikan lagu berdasarkan kemiripan fitur audio, bukan berdasarkan rating atau interaksi pengguna.

---

## ⚙️ Cara Kerja Sistem

Setiap lagu direpresentasikan sebagai vektor fitur audio yang terdiri dari:

- acousticness  
- danceability  
- energy  
- tempo  
- valence  
- instrumentalness  
- loudness  

Kemudian, Annoy membangun struktur indeks dari vektor tersebut dan melakukan pencarian tetangga terdekat berdasarkan **jarak dalam ruang vektor**.

---

## 🔍 Inti Sistem

Sistem ini tidak memahami musik berdasarkan genre atau metadata secara langsung, melainkan hanya berdasarkan kemiripan fitur audio.

Dampaknya:
- Lagu dengan karakter suara yang mirip akan direkomendasikan bersama
- Rekomendasi bisa lintas genre (misalnya Movie → Classical → Opera)
- Fokus utama adalah kemiripan “audio similarity”, bukan label

---

## 🚀 Alur Proses

1. Memuat dataset (fitur audio + metadata)
2. Membangun indeks Annoy
3. Melakukan query pada satu lagu
4. Mengambil K tetangga terdekat
5. Menampilkan hasil rekomendasi (judul, artis, genre)

---

## 🎯 Versi Non-Filtered vs Filtered

### 🔹 Non-Filtered (Pure ANN)
- Menggunakan kemiripan audio saja
- Tidak mempertimbangkan genre
- Hasil lebih beragam dan eksploratif

### 🔹 Filtered (Dengan Genre)
- Menambahkan filter genre setelah proses retrieval
- Hanya menampilkan lagu dengan genre yang sama (jika tersedia)
- Hasil lebih sesuai dengan ekspektasi pengguna

---

## ⚖️ Parameter K (Jumlah Tetangga)

Parameter **K** menentukan jumlah kandidat yang diambil dari hasil pencarian.

- K kecil → hasil lebih ketat, tetapi bisa kehilangan kandidat relevan  
- K besar → lebih banyak kandidat, meningkatkan peluang menemukan lagu yang relevan setelah filtering  

Dalam implementasi ini:
- K retrieval dibuat lebih besar (misalnya 20)
- Hasil akhir yang ditampilkan dibatasi (misalnya top 5)

Hal ini dilakukan untuk menjaga keseimbangan antara **cakupan hasil dan relevansi**.

---

## ⏱️ Performa

Annoy dirancang untuk pencarian tetangga terdekat yang efisien:

- Proses build cepat  
- Query sangat cepat  
- Cocok untuk dataset besar  

---

## 📌 Insight Penting

Sistem ini menunjukkan bahwa:

> Kemiripan berdasarkan fitur audio tidak selalu selaras dengan label genre.

Namun, penggunaan filtering dapat meningkatkan relevansi hasil rekomendasi secara signifikan.

---

## 🧠 Teknologi yang Digunakan

- Python  
- NumPy  
- Pandas  
- Annoy  

---

## 📁 Catatan

Implementasi ini juga digunakan sebagai bagian dari perbandingan dengan:
- FAISS  
- HNSW  

untuk menganalisis trade-off antara kecepatan, akurasi, dan skalabilitas dalam sistem pencarian nearest neighbor.