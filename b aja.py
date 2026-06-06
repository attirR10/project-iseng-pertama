print("\n----SIGN UP----")

name = input("Masukkan Nama : ")
pw = int(input("Masukkan Password : "))

while True:
    print("\n----LOGIN----")
    name1 = input("Masukkan nama : ")
    pw1 = int(input("Masukkan kode : "))

    if pw1 == pw:
        break

    else:
        print("SALAH, Coba lagi")

print("selamat datang di app sederhana ini")
print("Untuk keluar pencet E atau e")

def kalkulator():
    print("\n------Kalkulator------")

    if opsi == "E" or opsi == "e":
        exit()

    while True:
        a0 = int(input("angka pertama : "))
        a1 = int(input("angka Kedua : "))

        opsi = input("\nA.tambah \nB.kurang \nC.kali \nD.bagi")

        if opsi == "A" or opsi == "a":
            hasil = a0 + a1
            print("Hasil : ", hasil)

        elif opsi == "B" or opsi == "b":
            hasil = a0 - a1
            print("Hasil : ", hasil)
        
        elif opsi == "C" or opsi == "c":
            hasil = a0 * a1
            print("Hasil : ", hasil)
        
        elif opsi == "D" or opsi == "d":
            hasil = a0 / a1
            print("Hasil : ", hasil)

            if a1 == 0:
                print("Invalid")

        else:
            print("ulang lagi")

def struk_kasir():
    print("\n-----Struk Kasir-----")

    item = input("Masukkan Barang : ")
    price = int(input("Masukkan Harga : "))
    lot = int(input("Masukkan Jumlah : "))

    hasil = price * lot
    print("Hasil : ", hasil)

    while True:
        print("\n----------------")

        item1 = input("Masukkan Barang : ")
        price1 = int(input("Masukkan Harga : "))
        lot1 = int(input("Masukkan Jumlah : "))
      
        hasil = price * lot
        print("Hasil : ", hasil)

        if item and item1 == "E" or item and item1 == "e":
            print("Operation End")
            exit()

def data():
    import pandas as pd

    nama = []
    umur = []
    pengalaman = []

    print("-----DATA-----")

    while True:
        data0 = input("Nama : ")
        data1 = int(input("Umur : "))
        data2 = int(input("Pengalaman : "))

        nama.append(data0)
        umur.append(data1)
        pengalaman.append(data2)

        df = pd.DataFrame({"nama": nama, "umur": umur, "pengalaman": pengalaman})
        print(df)

print("\nFitur :")
Menu = input("\nA.Kalkulator \nB.Struk kasir \nC.Data \nD.Exit \n=")

if Menu == "A" or Menu == "a":
    kalkulator()
elif Menu == "B" or Menu == "b":
    struk_kasir()
elif Menu == "C" or Menu == "c":
    data()
elif Menu == "D" or Menu == "d":
    exit()
else:
    print("pilihan salah")

