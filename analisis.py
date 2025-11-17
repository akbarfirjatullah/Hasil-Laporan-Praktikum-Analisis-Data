import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('D:/CODING2EPIK/Practice Projects/PYTHON/Analysis/nilai_siswa.csv')

print("=== INFORMASI DATA ===")
data.info()
print("\n")

print("=== 5 BARIS PERTAMA ===")
print(data.head())
print("\n")

print("=== STATISTIK DESKRIPTIF ===")
print(data.describe())
print("\n")

print("=== UKURAN STATISTIK ===")
print("Rata-rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])
print("\n")

print("=== NILAI MATEMATIKA ===")
matematika = data[data['Matpel'] == 'Matematika']
print(matematika)
print("\n")

print("=== NILAI BAHASA INGGRIS ===")
bahasa_inggris = data[data['Matpel'] == 'Bahasa Inggris']
print(bahasa_inggris)
print("\n")

print("=== NILAI BAHASA INDONESIA ===")
bahasa_indonesia = data[data['Matpel'] == 'Bahasa Indonesia']
print(bahasa_indonesia)
print("\n")

print("=== NILAI PRODUKTIF ===")
produktif = data[data['Matpel'] == 'Produktif']
print(produktif)
print("\n")

print("=== NILAI MAKSIMUM DAN MINIMUM PER MATA PELAJARAN ===")
print(data.groupby('Matpel')['Nilai'].agg(['max', 'min']))
print("\n")

print("Membuat diagram batang...")
rata = data.groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar')
plt.title('Rata-Rata Nilai per Mata Pelajaran')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("Membuat boxplot...")
sns.boxplot(x='Matpel', y='Nilai', data=data)
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\n=== ANALISIS SELESAI ===")

# === PERTANYAAN ===
# 1. Mapel mana yang memiliki rata-rata nilai tertinggi?
print(data.groupby('Matpel')['Nilai'].mean().sort_values(ascending=False))
# JAWABAN: MATEMATIKA PALING TERTINGGI 

# 2. Mapel mana yang memiliki nilai terendah?
print(data.groupby('Matpel')['Nilai'].min())
# JAWABAN: BAHASA INDONESIA PALING TERENDAH