import pandas as pd
import matplotlib.pyplot as plt

bulan = []
Return = []

print("PRESS 'E' TO EXIT FROM THIS PROGRAM")
while True:
        data1 = input('BULAN: ')
        if data1 == 'E' or data1 == 'e':
             print('OPERATION_ENDED')
             break

        try:
            data2 = int(input('RETURN: '))
        except ValueError:
            print('INTEGER_HAS_NOT_VALID')
            continue

        bulan.append(data1) 
        Return.append(data2)

df = pd.DataFrame({'BULAN': bulan, 'RETURN': Return})
print(df)

plt.figure(figsize=(8, 5))
plt.plot(bulan, Return, marker='o')
plt.ylabel('RETURN')
plt.xlabel('BULAN')
plt.grid(True)
plt.show()