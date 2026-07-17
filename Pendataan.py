import pandas as pd

print("PENDATAAN")

nama  = []
umur = []
status = []

def cek(umur):
        if umur < 16:
            return 'Gak boleh masuk'
        elif umur == 16:
            return  "Sedang dipertimbangkan"
        else:
            return "Boleh Masuk"


while True:
    data1 = str(input('Masukkan Nama: '))
    data2 = int(input('Masukkan Umur: '))

    nama.append(data1)
    umur.append(data2)
    status.append(cek(data2))

    df = pd.DataFrame({'Nama': nama, 'Umur': umur, 'Status': status})
    print(df)