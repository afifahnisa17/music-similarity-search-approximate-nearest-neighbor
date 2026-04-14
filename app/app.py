import streamlit as st
import numpy as np
import pandas as pd
import faiss
import time

# --- 1. CONFIGURATION & UI SETUP ---
st.set_page_config(page_title="Music Recommendation System", layout="wide")
st.title("🎵 Music Recommender (FAISS)")

# --- 2. DATA LOADING (CACHED) ---
# Menggunakan decorator cache agar data tidak di-load ulang setiap kali widget berubah
@st.cache_data
def load_data():
    X = np.load("../0_data/processed/features.npy")
    meta = pd.read_csv("../0_data/processed/meta.csv")
    return X, meta

@st.cache_resource
def build_faiss(X):
    dim = X.shape[1]
    index = faiss.IndexFlatL2(dim)
    start = time.time()
    index.add(X)
    build_time = time.time() - start
    return index, build_time

# Jalankan loading
try:
    X, meta = load_data()
    index, build_time = build_faiss(X)
    st.sidebar.success(f"FAISS Index built in {build_time:.4f}s")
except Exception as e:
    st.error(f"Error loading data: {e}")
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

# Menyiapkan query vector
query_vector = X[query_idx].reshape(1, -1)

# Eksekusi pencarian
indices, distances, query_time = query_faiss(index, query_vector, k=k_neighbors)

# --- 5. DISPLAY RESULTS ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Current Track")
    current_track = meta.iloc[query_idx]
    st.info(f"**{current_track['track_name']}**\n\nArtist: {current_track['artist_name']}\n\nGenre: {current_track['genre']}")

with col2:
    st.subheader("Performance Metrics")
    st.metric("Query Time", f"{query_time:.6f}s")
    st.metric("Total Data", f"{len(X)} rows")

st.divider()
st.subheader("🎧 Recommended for You")

# Tampilkan hasil dalam DataFrame agar rapi
results = []
for i in indices[0]:
    if i == query_idx: continue  # Skip lagu yang sama dengan query
    results.append({
        "Track Name": meta.iloc[i]["track_name"],
        "Artist": meta.iloc[i]["artist_name"],
        "Genre": meta.iloc[i]["genre"]
    })

st.table(pd.DataFrame(results))