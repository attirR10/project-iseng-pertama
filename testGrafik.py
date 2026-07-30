import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'D:\Latihan coding\contoh.csv')
data.head()
df = pd.DataFrame(data)

hobi1 = df['Hobi'].head(5)
jumlah1 =df['Jumlah'].head(5)

sns.barplot(x='Hobi', y='Jumlah', data=data)
plt.title("HOBI_FAVORIT")
plt.show()