# UPDATE table_name
# SET column1 = value1, column2 = value2, ...
# WHERE condition;
import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
conn = sqlite3.connect('database_hewan.db')
cursor = conn.cursor()

# Data yang ingin diubah
nama_hewan = 'Komodo'
asal_baru = 'Nusa Tenggara Timur'

# Menjalankan query UPDATE
cursor.execute(f"UPDATE HEWAN SET asal = '{asal_baru}' WHERE nama_hewan = '{nama_hewan}'")
conn.commit()

# Menampilkan pesan setelah update berhasil
if cursor.rowcount > 0:
    print(f"Data Hewan dengan NAMA {nama_hewan} berhasil diupdate.")
else:
    print(f"Tidak ada data Hewan dengan NAMA {nama_hewan}.")

# Menutup koneksi
conn.close()
