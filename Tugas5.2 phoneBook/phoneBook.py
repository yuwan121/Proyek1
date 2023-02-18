""" Nama : Muhamad Fahri Yuwan Dwi Putra
    Kelas: 1B
    NIM  : 221524047
"""

kontak = {}

def pilihan_input(pil):
    if pil == '1':
        nama = input("\nMasukkan Nama : ")
        no_telp = input("\nMasukkan No Teleponnya : ")
        kontak[nama] = {"no_telp": no_telp}
        menyimpan_file()
    if pil == '2':
        isCheck = False
        nama_comp = input("Kontak yang mau Anda hapus : ")
        for nama in kontak:
            if nama == nama_comp:
                kontak.pop(nama)
                menyimpan_file()
                isCheck = False
                break
            else:
                isCheck = True
        if isCheck == True:
            print("Kontak yang Anda maksud tidak ada\n")
    if pil == '3':
        isCheck = False
        nama_comp = input("Kontak yang mau Anda cari : ")
        for nama in kontak:
            if nama == nama_comp:
                print("\n")
                print(nama, kontak[nama]["no_telp"])
                print("\n")
                isCheck = False
                break
            else:
                isCheck = True
        if isCheck == True:
            print("Kontak yang Anda maksud tidak ada\n")
    if pil == '4':
        print("\nDaftar Kontak:\n")
        for nama in kontak:
            print(f"{nama}: {kontak[nama]['no_telp']}")
        print("\n")
    if pil == '99':
        print("Dadahhhhhh~~~! Sayaannggg")

def menyimpan_file():
    file = open("phoneBook.txt", "w")
    for nama in kontak:
        file.write(f"{nama},{kontak[nama]['no_telp']}\n")
    print("Pembaruan kontak berhasil dilakukan\n")
    file.close()

def membuat_file():
    file = open("phoneBook.txt", "w")
    nama = input("\nMasukkan Nama : ")
    no_telp = input("\nMasukkan No Teleponnya : ")
    kontak[nama] = {"no_telp": no_telp}
    file.write(f"{nama},{no_telp}\n")
    file.close()

def tampilan_inputan():
    print("===========My PhoneBook===========")
    print("1. Menambambah/Mengganti nomber telepon kontak\n")
    print("2. Menghapus kontak tertentu\n")
    print("3. Mencari kontak tertentu\n")
    print("4. Menampilkan kontak\n")
    print("99. Keluar program\n")

def read_file():
    file = open("phoneBook.txt", "r")
    lines = file.readlines()
    for line in lines:
        data = line.strip().split(",")
        nama = data[0]
        no_telp = data[1]
        kontak[nama] = {"no_telp": no_telp}

import os

"""deklarasi variabel"""
nama_file = "phoneBook.txt"
isValid = False

while isValid == False:
    if os.path.exists(nama_file):
        read_file()
        pilihan = 0
        while int(pilihan) != 99:
            tampilan_inputan()
            pilihan = input ("\nPilihan Anda : ")
            pilihan_input(pilihan)
        isValid = True
    else:
        print("Membuat kontak baru dari awal, karena file phoneBook.txt tidak ada ")
        membuat_file()
