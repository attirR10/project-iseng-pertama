print("\n---APP SEDERHANA 2---")
print("MENU")

while True:
    Menu = input("\nA.kalkulator \nB.struk belanja \nC.inventaris \nD.Kurs \nE.Exit \n=")

    def kalkulator():
        while True:
            print("\n---KALKULATOR---")

            a01 = int(input("Masukkan Angka 1 : "))
            a02 = int(input("Masukkan Angka 2 : "))

            opsi = input("OPERASI \nA.Tambah \nB.Kurang \nC.Kali \nD.Bagi \nE.Exit \n=")

            if opsi == "A" or opsi == "a":
                hasil = a01 + a02
                print("Hasil = ", hasil)

            elif opsi == "B" or opsi == "b":
                hasil = a01 - a02
                print("Hasil = ", hasil)

            elif opsi == "C" or opsi == "c":
                hasil = a01 * a02
                print("Hasil = ", hasil)

            elif opsi == "D" or opsi == "d":
                hasil = a01 / a02
                print("Hasil = ", hasil)

            if a02 == 0:
                print("Invalid")

            else:
                print("Coba lagi")

    def struk_belanja():
        print("\n---Struk Belanja---")

        item = str(input("Masukkan Nama Barang : "))
        price = int(input("Masukkan Harga BArang : "))
        stik = int(input("Masukkan Jumlah barang : "))

        hasil = price * stik
        print("TOTAL = ", hasil)

        while True:
            print("\n-------------------")
            items = str(input("Masukkan Nama Barang : "))
            prices = int(input("Masukkan Harga BArang : "))
            stiks = int(input("Masukkan Jumlah barang : "))

            hasil = prices * stiks
            print("TOTAL = ", hasil)

            if items == "E" or items == "e":
                exit()

    def inventaris():
        import pandas as pd
        
        barang = []
        harga = []
        jumlah = []
        
        while True:
            print("---INVENTARIS---")
            data0 = str(input("Masukkan nama Barang : "))
            data1 = int(input("Masukkan Harga Barang :"))
            data2 = int(input("Masukkan Jumlah Barang : "))

            barang.append(data0)
            harga.append(data1)
            jumlah.append(data2)

            df = pd.DataFrame({"Barang": barang, "Harga": harga, "Jumlah": jumlah})
            print(df)

            if data0 == "E" or data0 == "e":
                break

    def kurs():
        from forex_python.converter import CurrencyRates
        
        while True:
            print("\n---KURS---")
            kurs = CurrencyRates()
            jumlah = int(input("Masukkan Jumlah Uang : "))
        
            dari = input("Dari mata uang : ").upper()
            ke = input("Ke mata Uang : ").upper()

            print(jumlah, dari, "menjadi", ke)
            hasil = kurs.convert(dari, ke, jumlah)
            print(hasil)

            if jumlah == "E" or jumlah == "e":
                break

    if Menu == "A" or Menu == "a":
        kalkulator()
        break
    elif Menu == "B" or Menu == "b":
        struk_belanja()
        break
    elif Menu == "C" or Menu == "c":
        inventaris()
        break
    elif Menu == "D" or Menu == "d":
        kurs()
        break
    elif Menu == "E" or Menu == "e":
        exit()
    else:
        print("Karakter Salah!")    