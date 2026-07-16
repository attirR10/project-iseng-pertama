while True:
    print("\n---KALKULATOR MARK---")

    a = int(input('Angka Kesatu: '))
    b = int(input('Angka Kedua: '))
    ops = input("Operasi: \ntambah, \nkurang, \nkali, \nbagi, \nmodulos \n=")

    def hasil(a, b):
        if ops =='+' or ops == 'tambah':
            return a + b
        elif ops == '-' or ops == 'kurang':
            return a - b
        elif ops == 'x' or ops == 'kali':
            return a * b
        elif ops == ":" or ops == 'bagi':
            return a / b
        elif ops == '%' or ops == 'modulos':
            return a % b
        else: 
            return 'not valid'.upper()
    
    print(hasil(a, b))