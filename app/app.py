import streamlit as st
import numpy as np
import pandas as pd
import faiss
import time
import os

# --- 1. CONFIGURATION & UI SETUP ---
st.set_page_config(page_title="Music Recommendation System", layout="wide")
st.title("🎵 Music Recommender (FAISS)")

# Mengatur path secara dinamis agar aman di lokal maupun cloud
current_dir = os.path.dirname(os.path.abspath(__file__))


# --- 2. DATA LOADING (CACHED) ---
@st.cache_data
def load_data():
    X = np.load("0_data/processed/features.npy")
    meta = pd.read_csv("0_data/processed/meta.csv")
    # Memeriksa sinkronisasi data dan metadata sesuai skrip asli
    assert len(X) == len(meta)
    return X, meta

@st.cache_resource
def build_faiss_index(X):
    dim = X.shape[1]
    index = faiss.IndexFlatL2(dim)
    start = time.time()
    index.add(X)
    build_time = time.time() - start
    return index, build_time

# Eksekusi Loading
try:
    X, meta = load_data()
    index, b_time = build_faiss_index(X)
    st.sidebar.success(f"FAISS Index built in {b_time:.4f}s")
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.info("Pastikan struktur folder sudah benar: /0_data/processed/ di root repositori.")
    st.stop()

# --- 3. SIDEBAR / INPUT ---
st.sidebar.header("Query Settings")
query_idx = st.sidebar.number_input("Pilih Index Lagu", min_value=0, max_value=len(meta)-1, value=10)
k_neighbors = st.sidebar.slider("Jumlah Rekomendasi", 5, 50, 20)

# --- 4. QUERY LOGIC ---
def query_faiss(index, query, k=20):
    start = time.time()
    distances, indices = index.search(query, k)
    query_time = time.time() - start
    return indices, distances, query_time

# Menyiapkan query vector sesuai skrip asli
query_vector = X[query_idx].reshape(1, -1)

# Eksekusi pencarian
indices, distances, q_time = query_faiss(index, query_vector, k=k_neighbors)

# --- 5. DISPLAY RESULTS ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎵 Query Track")
    q_track = meta.iloc[query_idx]
    # Format tampilan informasi query
    st.info(f"**{q_track['track_name']}** \n"
            f"Artist: {q_track['artist_name']}  \n"
            f"Genre: {q_track['genre']}")

with col2:
    st.subheader("⚡ Performance Metrics")
    st.metric("Query Time", f"{q_time:.6f}s")
    st.metric("Build Time", f"{b_time:.4f}s")

st.divider()
st.subheader("🎧 Recommendations")

# 1. Membangun list hasil awal
results = []
for i in indices[0]:
    if i == query_idx: 
        continue
    
    results.append({
        "Track Name": meta.iloc[i]["track_name"],
        "Artist": meta.iloc[i]["artist_name"],
        "Genre": meta.iloc[i]["genre"]
    })

if results:
    df_results = pd.DataFrame(results)
    
    # Ambil nama genre dari lagu query
    target_genre = meta.iloc[query_idx]["genre"]
    
    df_results['is_same_genre'] = df_results['Genre'] == target_genre
    df_results = df_results.sort_values(by='is_same_genre', ascending=False)
    
    # Hapus kolom pembantu sebelum ditampilkan agar UI bersih
    df_output = df_results.drop(columns=['is_same_genre'])
    
    st.table(df_output)

