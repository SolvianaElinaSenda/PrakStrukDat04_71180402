import json

buka= open('karyawan.json', 'r')
data = json.load(buka) # file yang dibuka lalu dibaca
for karyawan in data:
    print(karyawan)

#Tutup file
buka.close()


# MENULIS DATA YANG DIMASUKAN OLEH USER KE DALAM FILE KARYAWAN
file_json = open('karyawan.json', 'a+')

n = int(input("Masukan jumlah karyawan: "))
for i in range(n):
    nama = input("Masukan nama: ")
    alamat = input("Masukan alamat: ")
    kolega = int(input("Masukan jumlah kolega: "))
    for j in range(kolega):
        if kolega>0:
            nama_kolega=input("Masukan nama kolega: ")
        else:
            print("Jumlah Kolega Minimal 1")

    print("===Data Berhasil Ditambahkan===")

file_json.write( + '\n')

file_json.close()

