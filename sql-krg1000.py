import sqlite3

koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()
kursor.execute("SELECT * FROM HEWAN WHERE jml_sekarang <= 1000 ")
baris_table = kursor.fetchall()

print("Data Hewan:")
print("=============================================================================================================================")
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("id_hewan", " ""nama_hewan", "jenis", "asal", "jml_sekarang", "thn_ditemukan"))
print("-----------------------------------------------------------------------------------------------------------------------------")
for baris in baris_table:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))

koneksi.close()
