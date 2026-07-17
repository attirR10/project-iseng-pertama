print("---APP SEDERHANA 3 ---")
#project training series
while True:
    menu = str(input('SUITE-APP: \nA.Kalkulator \nB.Data \nE.exit \n'))
     
    def kalkulator():
        while True:
            try:
                a1 = int(input("ANGKA-KESATU: "))
            except ValueError:
                print("NOT-VALID")
                continue
            try:
                a2 = int(input("ANGKA-KEDUA: "))
            except ValueError:
                print("NOT-VALID")
                continue
            
            opsJumlah = input("\nOPERASI \nTambah \nKurang \nKali \nBagi \nExit \n= ")

            if opsJumlah == 'Tambah' or opsJumlah == 'tambah':
                hasil = a1 + a2
                print(hasil)
            elif opsJumlah == 'kurang' or opsJumlah == 'Kurang':
                hasil = a1 - a2 
                print(hasil)
            elif opsJumlah == 'kali' or opsJumlah == 'Kali':
                hasil = a1 * a2 
                print(hasil)
            elif opsJumlah == 'bagi' or opsJumlah == 'Bagi':
                hasil = a1 / a2 
                print(hasil)
            elif opsJumlah == 'exit' or opsJumlah == 'Exit':
                print('\nOPERATION-ENDED')
                break        
            else:
                print ("OPTION NOT VALID")
            
    def data():
        import pandas as pd
            
        nama = []
        stock = []
        kondisi = []

        def cek(stock):
            if stock < 50:
                return 'KRITIS'
            elif stock == 50:
                return 'AMAN'
            elif stock > 50:
                return 'SURPLUS'
            else:
                return "NOT-VALID"
       
        while True:
            data1 = str(input("NAMA BARANG: "))
            try:
                data2 = int(input("STOCK TERSISA: "))
            except ValueError:
                print('INTEGER HAS NOT DETECTED')
                continue

            nama.append(data1)
            stock.append(data2)
            kondisi.append(cek(data2))

            if data1 == 'E' or data1 == 'e':
                break

            df = pd.DataFrame({'Barang': nama, 'Stock': stock, 'Kondisi': kondisi})
            print(df)

    if menu == 'a' or menu == 'A':
        kalkulator()
        break
    elif menu == 'B' or menu == 'b':
        data()
        break
    elif menu == 'e' or menu == 'E':
        print('OPERATION ENDED')
        break
