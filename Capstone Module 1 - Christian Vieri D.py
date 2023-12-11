import random

print('Selamat Datang di Perpustakaan Universitas Purwadhika')

header = [
    "ID Buku",
    "Judul Buku",
    "Jenis Buku",
    "Penerbit Buku",
    "Status Buku"
]

data = [
    ["PTUP-DS-31", "DS Intro", "DS", "Gramedia", "Tersedia"],
    ["PTUP-WD-74", "WD Intro", "WD", "Balai Pustaka", "Terpinjam"],
    ["PTUP-UX-31", "UI/X Intro", "UI/X", "Erlangga", "Tersedia"],
    ["PTUP-DM-67", "DM Intro", "DM", "Gagas Media", "Hilang/Rusak"],
]

daftar_buku = []
for j in range(len(data)):
    buku = {}
    for k in range(len(data[j])):
        buku.update({header[k]:data[j][k]})
    daftar_buku.append(buku)

# Fungsi Menampilkan Daftar Buku
def list_daftar_buku():
    nomor = 0
    print("NOID Buku\t Judul Buku\t Jenis Buku\t Penerbit\t Status Buku")
    for j in daftar_buku:
        print (f'{nomor}{j["ID Buku"]}\t {j["Judul Buku"]}\t {j["Jenis Buku"]}\t\t {j["Penerbit Buku"]}\t {j["Status Buku"]}')
        nomor+=1

# Fungsi Menghapus Buku
def hapus_buku():
    while True:
        try:
            list_daftar_buku()
            angka_hapus = int(input('Masukkan angka pertama:'))
            del  daftar_buku[angka_hapus]
            break
        except:
            print('Input hanya boleh angka!')

# Fungsi Menambahkan Buku
def menambahkan_buku():
    ID1 = 'PTUP-'
    ID2 = ' '
    ID3 = str(random.randint(10,99))

    input_tambah_judul = str(input('Masukkan Judul Buku Baru: '))

    while True:

        input_tambah_jenis = str(input('Masukkan Jenis Buku Baru (Digital Marketing, Data Science, Web Development, UI/UX): '))
        if input_tambah_jenis.upper() == 'DIGITAL MARKETING':
            ID2='DM'
            input_tambah_jenis = 'DM'
            break
        elif input_tambah_jenis.upper() == 'DATA SCIENCE':
            ID2='DS'
            input_tambah_jenis = 'DS'
            break
        elif input_tambah_jenis.upper() == 'WEB DEVELOPMENT':
            ID2='WD'
            input_tambah_jenis = 'WD'
            break
        elif input_tambah_jenis.upper() == 'UI/UX':
            ID2='UX'
            input_tambah_jenis = 'UX'
            break
        else: 
            print("Mohon masukkan jenis buku yang benar.")


    input_tambah_id = str(ID1+ID2+"-"+ID3) 
    input_tambah_penerbit = str(input('Masukkan Penerbit Buku: '))

    while True:
        
        input_tambah_status = str(input('Masukkan Status Buku Baru (Tersedia, Terpinjam, Hilang/Rusak): '))
        if input_tambah_status.upper() == 'TERSEDIA' or input_tambah_status.upper() == 'TERPINJAM' or input_tambah_status.upper() == 'HILANG/RUSAK':
            break
        else: 
            print('Mohon Masukkan Tersedia,Terpinjam,Hilang/Rusak! ')
        


    buku_baru = {"ID Buku":input_tambah_id,"Judul Buku":input_tambah_judul, "Jenis Buku":input_tambah_jenis, "Penerbit Buku": input_tambah_penerbit, "Status Buku": input_tambah_status.capitalize()}

    daftar_buku.append(buku_baru)

# Fungsi Meng-update Elemen pada Buku
def update_buku():
    while True:
        try:
            while True:
                try:
                    list_daftar_buku()
                    angka_update = int(input('Masukkan Digit Angka Pertama Dari Buku Yang Ingin Di Update: '))
                    if(angka_update>len(data) or angka_update<0):
                        print(f'Masukkan Angka 0-{len(data)}.')
                    else: 
                        break
                except:
                    print('Masukkan Digit Angka Pertama Dari Buku Yang Ingin Di Update!')
                
            while True:
                try:
                    print(''' 
            1. Update Judul Buku
            2. Update Penerbit Buku
            3. Update Status Buku
            4. Keluar Update
            ''')
                
                    update_menu = int(input('Masukkan angka pada elemen buku yang ingin diupdate:'))

                    if update_menu==1:
                        judul_baru = input('Masukkan Judul Buku Yang Ingin Di Update:')
                        daftar_buku[angka_update]["Judul Buku"]= judul_baru.capitalize()
                        list_daftar_buku()

                    elif update_menu==2:
                        penerbit_baru = input('Masukkan Penerbit Buku Yang Ingin Di Update:')
                        daftar_buku[angka_update]["Penerbit Buku"]= penerbit_baru.capitalize()
                        list_daftar_buku()


                    elif update_menu==3:
                        while True:
                            status_baru = (input('Masukkan Status Buku Baru (Tersedia, Terpinjam, Hilang/Rusak): '))
                            if status_baru.upper() == 'TERSEDIA' or status_baru.upper() == 'TERPINJAM' or status_baru.upper() == 'HILANG/RUSAK':
                                daftar_buku[angka_update]["Status Buku"]= status_baru.capitalize()
                                list_daftar_buku()
                                break
                            else: 
                                print('Mohon Masukkan Tersedia,Terpinjam,Hilang/Rusak! ')

                    elif update_menu==4:
                        break

                    else: 
                        print('Mohon Input Angka 1/2/3/4!')

                except:
                    print('Mohon input angka 1/2/3/4!')
            break
        
        except: 
            print('Masukkan inputan yang benar.')

#-------------------------------------------------------------------------------------------------------------------------------------



while True:
    try:
        print('''
        List Menu:
        1. Menampilkan Daftar Buku
        2. Menghapus Buku
        3. Menambah Buku
        4. Merubah Elemen Pada Buku
        5. Keluar Program''')
        angka = int(input('Masukkan Angka yang diinginkan: '))

# 1. Menu Read
        if angka == 1:
            list_daftar_buku()

# 2. Menu Delete
        elif angka == 2:
            hapus_buku()
# 3. Menu Create
        elif angka == 3:
            menambahkan_buku()
            list_daftar_buku()

# 4.Menu Update
        elif angka == 4:
            update_buku()

# 5. Keluar Program
        elif angka == 5:
            break

    except: print('Mohon masukkan inputan yang benar.')