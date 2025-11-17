## **LAPORAN PRAKTIKUM ANALISIS DATA & VISUALISASI DATA**

## **Identitas**
- **Mata Pelajaran:** Koding Kecerdasan Artifisial
- **Kelas:** XI RPL
- **Nama:** Muhammad Aulia Akbar Firjatullah

---

## **💻 Kode Program**

```python
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
```

---

## **📊 Output Program**

### **1. Informasi Data**
```
=== INFORMASI DATA ===
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 22 entries, 0 to 21
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   Nama    22 non-null     object
 1   Matpel  22 non-null     object
 2   Nilai   22 non-null     int64
dtypes: int64(1), object(2)
memory usage: 660.0+ bytes
```

### **2. Lima Baris Pertama**
```
=== 5 BARIS PERTAMA ===
     Nama            Matpel  Nilai
0     Ade  Bahasa Indonesia     87
1    Aira  Bahasa Indonesia     88
2    Badi    Bahasa Inggris     78
3    Cyla    Bahasa Inggris     90
4  Khansa        Matematika     98
```

### **3. Statistik Deskriptif**
```
=== STATISTIK DESKRIPTIF ===
           Nilai
count  22.000000
mean   86.318182
std     6.066193
min    75.000000
25%    85.000000
50%    86.500000
75%    90.000000
max    98.000000
```

### **4. Ukuran Statistik**
```
=== UKURAN STATISTIK ===
Rata-rata: 86.31818181818181
Median: 86.5
Modus: 85
```

### **5. Nilai Maksimum dan Minimum per Mata Pelajaran**
```
=== NILAI MAKSIMUM DAN MINIMUM PER MATA PELAJARAN ===
                  max  min
Matpel                    
Bahasa Indonesia   88   87
Bahasa Inggris     90   78
Matematika         98   85
Produktif          90   75
```

### **6. Visualisasi Data**

**Diagram Batang - Rata-Rata Nilai per Mata Pelajaran:**

![Bar Chart](screenshot_bar_chart.png)
*Keterangan: Grafik menunjukkan rata-rata nilai setiap mata pelajaran*

**Boxplot - Sebaran Nilai per Mata Pelajaran:**

![Boxplot](screenshot_boxplot.png)
*Keterangan: Boxplot menunjukkan distribusi, median, dan outlier nilai per mata pelajaran*

---

## **📈 Analisis dan Pertanyaan**

### **1. Mapel mana yang memiliki rata-rata nilai tertinggi?**

**Jawaban:** Mata pelajaran **Matematika** memiliki rata-rata nilai tertinggi yaitu sekitar **91.5**. Hal ini menunjukkan bahwa siswa memiliki pemahaman yang sangat baik dalam mata pelajaran Matematika dan kemampuan numerik mereka cukup kuat.

---

### **2. Mapel mana yang memiliki nilai terendah?**

**Jawaban:** Mata pelajaran **Bahasa Indonesia** memiliki nilai terendah yaitu **75**. Ini mengindikasikan bahwa ada siswa yang mengalami kesulitan dalam mata pelajaran Produktif dan memerlukan bimbingan tambahan untuk meningkatkan pemahamannya.

---

### **3. Bagaimana visualisasi membantu dalam memahami data?**

**Jawaban:** Visualisasi data sangat membantu dalam memahami informasi secara lebih cepat dan efektif. Misalnya, diagram batang memudahkan kita untuk membandingkan rata-rata nilai antar mata pelajaran secara visual hanya dalam sekali pandang, sehingga kita bisa langsung mengetahui mana yang memiliki performa terbaik atau perlu peningkatan. Selain itu, boxplot menyajikan informasi yang lebih mendetail, seperti median, kuartil atas dan bawah, rentang nilai, outlier, dan konsistensi nilai siswa per mata pelajaran. Grafik juga lebih efisien dipahami dibandingkan tabel angka karena otak manusia lebih cepat memproses informasi visual. Dengan visualisasi, pola, tren, dan anomali dalam data dapat terlihat lebih jelas, serta memudahkan penyampaian insight kepada guru, kepala sekolah, atau orang tua.

---

## **🤔 Refleksi Siswa**

### **1. Apa hal baru yang kamu pelajari dari kegiatan analisis dan visualisasi data?**

**Jawaban:** Dalam kegiatan analisis dan visualisasi data ini saya mempelajari banyak hal baru terutama terkait penggunaan library Python seperti Pandas untuk manipulasi data serta Matplotlib dan Seaborn untuk membuat grafik dan visualisasi statistik lanjutan Saya juga memahami pentingnya statistik deskriptif seperti mean median modus dan standar deviasi untuk menggambarkan karakteristik data Selain itu saya belajar melakukan grouping dan aggregation menggunakan fungsi groupby yang membantu dalam menemukan nilai maksimum minimum atau rata-rata berdasarkan kategori tertentu Kemampuan membaca dan menginterpretasikan visualisasi seperti boxplot juga menjadi hal baru termasuk memahami konsep outlier kuartil dan sebaran data Dari kegiatan ini saya menyadari pentingnya data-driven decision making di mana keputusan bisa dibuat secara lebih objektif berdasarkan hasil analisis Secara keseluruhan saya memahami alur lengkap seorang data analyst mulai dari membaca data eksplorasi analisis statistik hingga visualisasi hasil

---

### **2. Kesulitan apa yang kamu alami dalam membuat grafik?**

**Jawaban:** Dalam proses membuat grafik, saya mengalami beberapa kesulitan yang menjadi pengalaman berharga. Misalnya, saya sempat mendapati error `KeyError` karena salah menulis nama kolom—saya menulis `'Mapel'` padahal kolom aslinya bernama `'Matpel'`, yang mengingatkan saya pentingnya ketelitian dalam penulisan kode. Saya juga sempat salah penggunaan sintaks import dengan menulis `__pandas__` yang seharusnya hanya `pandas`. Selain itu, label pada sumbu x sempat tumpang tindih karena nama mata pelajaran yang panjang, sehingga saya harus belajar mengatur rotasi dengan `rotation=45` dan menggunakan `tight_layout()` agar grafik terlihat rapi. Saya juga perlu memahami berbagai parameter dalam fungsi plotting seperti `kind`, `x`, `y`, dan `data`, yang awalnya membingungkan. Tidak hanya itu, saya pernah lupa menambahkan `plt.show()` sehingga grafik tidak muncul, dan kemudian belajar cara menyimpan grafik menggunakan `plt.savefig()` untuk dokumentasi. Meski banyak tantangan, dengan mencoba berkali-kali, membaca pesan error dengan teliti, dan mencari solusi di dokumentasi maupun Stack Overflow, saya akhirnya mulai memahami dan terbiasa dengan proses visualisasi data.


---

### **3. Menurut kamu AI apa membantu dalam analisis sebuah data?**

**Jawaban:** AI sangat membantu dalam analisis data karena mampu memproses data dengan cepat dan efisien, mengotomatisasi tugas-tugas seperti data cleaning, serta mengurangi kesalahan manusia. AI juga dapat mengenali pola yang sulit ditemukan secara manual, melakukan prediksi berdasarkan data historis, dan bahkan merekomendasikan visualisasi atau membuat dashboard otomatis. Dalam analisis teks, AI menggunakan NLP untuk menganalisis sentiment dan memahami feedback. Selain itu, AI mendukung personalisasi pembelajaran dan mampu mendeteksi anomali dalam data. Contohnya, dalam praktikum ini, library seperti Pandas, Matplotlib, dan Seaborn memanfaatkan algoritma yang dioptimalkan untuk komputasi cepat dan visualisasi informatif.


