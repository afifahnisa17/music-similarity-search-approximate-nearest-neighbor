import os
# Cek lokasi file ini
print(f"Lokasi file tes: {os.path.dirname(__file__)}")

# Cek lokasi yang kita tuju (naik satu level)
target = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "app", "app.py"))
print(f"Mencari app.py di: {target}")
print(f"Apakah file ditemukan? {os.path.exists(target)}")