print("----SIGN UP----")

name = input("Masukkan Nama : ")
age = int(input("Masukkan Umur : "))
pw = int(input("Masukkan Password : "))

if age < 15:
     print("Maaf, umur anda belum cukup untuk menggunakan aplikasi ini")
     exit()

else:
     print("ok")

while True:
     print("----LOGIN----")

     name1 = input("Masukkan nama : ")
     PW1 = int(input("Masukkan Password : "))

     if name1 == name and pw == PW1:
         print("oke masuk")
         break

     else:
          print("Maaf, password salah atau nama salah")

print("\nMenu")
print("INTRUKSI : Untuk keluar Pencet E")

def kalkulator():
     while True:  
          print("----Kalkulator----")

          a1 = int(input("Masukkan Angka kesatu : "))
          a2 = int(input("Masukkan Angka kedua : "))

          opsi = input("\nPilih Pengoperasian : \nA.Tambah \nB.Kurang \nC.Kali \nD.Bagi \nE.Keluar \n= ")

          if opsi == "A" or opsi == "a":
               hasil = a1 + a2
               print("Hasil : ", hasil)

          elif opsi == "B" or opsi == "b":
               hasil = a1 - a2
               print("Hasil : ", hasil)

          elif opsi == "C" or opsi == "c":
               hasil = a1 * a2
               print("Hasil : ", hasil)

          elif opsi == "D" or opsi == "d":
               hasil = a1 / a2
               print("Hasil : ", hasil)

               if a2 == 0:
                   print("Invalid")

          elif opsi == "E" or opsi == "e":
           break

          else:
               print("ulang lagi")

def manajemen():
     print("\n-----MANAJEMEN-----")

     items = input("Masukkan nama barang : ")
     price = int(input("Masukkan harga : "))
     lots = int(input("Masukkan Jumlah : "))

     hasil = price * lots
     print("Hasil : ", hasil)

     while True:
          print("----------------")

          
          items1 = input("Masukkan nama barang : ")
          price1 = int(input("Masukkan harga : "))
          lots1 = int(input("Masukkan Jumlah : "))

          hasil = price1 * lots1
          print("Hasil : ", hasil)

          if items == "E" or items == "e":
               print("operation end")
               break

def catatan():
     while True:
          print("\n-----CATATAN-----")

          catatn = input("masukkan catatan")
          print("Catatan hari ini adalah : ", catatn)

          if catatn == "E" or catatn == "e":
               break



MENU = input("\nA.kalkulator \nB.Manajemen \nC.Catatan \nD.Exit \n= ")

if MENU == "a" or MENU == "A":
     kalkulator()
elif MENU == "b" or MENU == "B":
     manajemen()
elif MENU == "c" or MENU == "C":
     catatan()
elif MENU == "d" or MENU == "D":
     exit()


