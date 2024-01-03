import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Membuat data set sederhana
data = {'Nama': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Usia': [25, 30, 35, 40, 45],
        'Gaji': [50000, 60000, 75000, 90000, 80000]}

# Membuat DataFrame menggunakan Pandas
df = pd.DataFrame(data)

# Menampilkan DataFrame
print("Data Awal:")
print(df)

# Menggunakan NumPy untuk menghitung rata-rata gaji
rata_rata_gaji = np.mean(df['Gaji'])
print("\nRata-rata Gaji:", rata_rata_gaji)

# Menambahkan kolom baru untuk menunjukkan status karyawan
df['Status'] = np.where(df['Usia'] >= 35, 'Senior', 'Junior')

# Menyimpan DataFrame yang telah diolah ke dalam file CSV
df.to_csv('data_karyawan.csv', index=False)

# Memvisualisasikan data menggunakan Matplotlib
plt.figure(figsize=(8, 5))
plt.bar(df['Nama'], df['Gaji'], color='blue')
plt.xlabel('Nama Karyawan')
plt.ylabel('Gaji')
plt.title('Grafik Gaji Karyawan')
plt.show()
