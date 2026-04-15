import pytest
from streamlit.testing.v1 import AppTest
import os

def get_app_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "app", "app.py"))

def test_music_recommender_flow():
    # 1. Inisiasi aplikasi dari file app.py
    at = AppTest.from_file(get_app_path(), default_timeout=30).run()

    # 2. Assert: Cek Judul
    assert at.title[0].value == "🎵 Music Recommender (FAISS)"

    # 3. Assert: Cek slide sidebar (defaultnya adalah 10)
    at.sidebar.slider[0].set_value(10).run()

    # 4. Assert: Cek apakah tabel hasil muncul
    assert len(at.table) > 0

    # 5. Assert: Query tidak boleh nol
    query_time_val = at.metric[0].value
    assert query_time_val != "0.0000000s"

def test_genre_logic():
    at = AppTest.from_file(get_app_path()).run()

    # Pilih index lagu
    at.sidebar.number_input[0].set_value(5).run()

    # Assert: Pastikan Track Info muncul
    assert len(at.info) > 0
    assert "Artist:" in at.info[0].value