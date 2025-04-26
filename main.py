    #"PROGRAM KONTAK"


def melihat_kontak():
    if kontak:
        for num, item in enumerate(kontak, start=1):
            print(f"{num}. {item['nama']}  {item['hp']} {item['email']}")
    else:
        print("Kontak masih Kosong")
        return 1

def menambah_kontak():
    nama = input("Masukan Nama Baru: ")
    hp = input("Masukan No HP Baru: ")
    email = input("Masukan Email Baru: ")
    kontak_baru = {'nama': nama, 'hp': hp, 'email': email}
    kontak.append(kontak_baru)
    print("Kontak baru berhasil ditambahkan!,ok")

def menghapus_kontak():
   if melihat_kontak() == 1:
       return
   else:
        i_hapus = int(input("Masukan Nomer Kontak yang ingin dihapus: "))
        del kontak[i_hapus - 1]
        print("Kontak baru berhasil dihapus!")


kontak1 ={'nama':"andi",'hp':'0871','email':'andi@python.com'}
kontak2 ={'nama':"budi",'hp':'0872','email':'budi@python.com'}
kontak3 ={'nama':"caca",'hp':'0873','email':'caca@python.com'}
kontak =[kontak1,kontak2,kontak3]

while True:
    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    Pilihan = input("Masukan Pilihan Menu Kontak (1,2,3, atau 4): ")

    if Pilihan == '1':
       # melihat kontak
        melihat_kontak()

    elif Pilihan == '2':
        # print("\nMenambahkan Kontak Baru")
        menambah_kontak()

    elif Pilihan == '3':
        #print("\nMenghapus Kontak")
       menghapus_kontak()

    elif Pilihan == '4':
        print("\nKeluar dari Kontak")
        break
    else:
        print("\n Anda memasukan pilihan yang salah")

