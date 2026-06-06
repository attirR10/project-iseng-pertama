import pandas as pd

nama = []
umur = []

while True:
    data = input("Nama : ")
    data1 = int(input("Umur : "))
     
    nama.append(data)
    umur.append(data1)

    df = pd.DataFrame({"nama": nama, "umur": umur})
    print(df)
