# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. 

### Permasalahan Bisnis

Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

### Cakupan Proyek

- Mengamati dataset pegawai yang dimiliki perusahaan tersebut
- Melakukan exploratory data pegawai, dan mencoba menemukan informasi menarik yang dapat menyelesaikan permasalahan
- Melakukan pembersihan data pegawai
- Membuat sebuah model machine learning yang dapat digunakan untuk memprediksi kemungkinan seorang pegawai akan keluar dari perusahaan tersebut berdasarkan parameter yang berkorelasi
- Melakukan evaluasi dari model machine learning tersebut
- Menemukan parameter apa saja yang mempengaruhi seorang pegawai keluar dari perusahaan tersebut
- Membuat business dashboard berbasis metabase

### Persiapan

Sumber data: employee_data.csv (https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)

Setup environment notebook:

```
pip install -r requirements.txt
```

Setup metabase:

```
docker build -t metabase-image .
docker run -d -p 3000:3000 --name metabase metabase-image
```

Metabase credentials:
Username: root@mail.com
Password: root123

## Business Dashboard

Pembuatan business dashboard telah menggunakan prinsip design dan integritas. Grafik yang tertera sudah ditentukan berdasarkan parameter yang paling krusial terhadap permasalahan yang dialami. Tata letak dari dashboard sudah sesuai dengan sweet spot, dan diurutkan berdasarkan parameter yang paling berpengaruh.

Dashboard terdiri dari:
1. Jumlah pegawai yang melakukan atrisi (keluar dari perusahaan)
2. Jumlah pegawai yang masih bekerja di perusahaan
3. Persentasi attrition rate berdasarkan income pegawai
4. Persentasi attrition rate berdasarkan umur pegawai
5. Persentasi attrition rate berdasarkan waktu lembur (overtime)

## Conclusion

**Kualitas Dataset**
- Dataset yang digunakan memiliki beberapa null values pada kolom Attrition. Dikarenakan kolom tersebut sangat berpengaruh terhadap permasalahan, maka tidak cocok jika menggunakan teknik imputasi untuk memaksakan tersedianya data tersebut. Sehingga lebih baik jika dihilangkan
- Dataset tidak terdapat duplikasi data
- Dataset terdapat outlier dalam beberapa kolom numerik. Akan tetapi, value yang dianggap outlier sangatlah wajar dikarenakan value tersebut benar adanya. Sebagai contoh terdapat beberapa outlier pada kolom monthly_income yang besarannya tinggi. Hal tersebut adalah wajar karena pegawai yang mendapat income tersebut adalah pegawai yang memiliki jabatan tinggi dan waktu bekerja yang sudah lama, sehingga sangatlah berbeda dengan pegawai yang lainnya. Keputusan untuk tidak menghapus outlier adalah karena data tersebut benar adanya, dan bukan merupakan kesalahan sistem.

**Interpretasi Faktor Utama Karyawan Meninggalkan Pekerjaan**
Berdasarkan hasil pemodelan menggunakan Random Forest dan analisis korelasi, berikut adalah tiga faktor utama yang paling signifikan mempengaruhi keputusan karyawan untuk meninggalkan perusahaan:

1. Monthly Income (Pendapatan Bulanan):
Merupakan faktor dengan skor kepentingan tertinggi. Karyawan dengan tingkat pendapatan yang lebih rendah cenderung memiliki risiko atrisi yang lebih tinggi. Hal ini menunjukkan bahwa kompensasi finansial tetap menjadi motivator utama dalam retensi karyawan.
2. Age (Usia):
Usia menunjukkan hubungan yang signifikan dengan atrisi. Karyawan yang lebih muda cenderung memiliki tingkat perputaran yang lebih tinggi, kemungkinan karena mereka masih dalam tahap eksplorasi karier atau mencari peluang pertumbuhan yang lebih cepat dibandingkan karyawan senior.
3. Total Working Years: Total masa kerja atau pengalaman karier secara keseluruhan turut menjadi penentu tingkat loyalitas. Karyawan dengan total masa kerja yang masih singkat umumnya memiliki risiko atrisi yang lebih tinggi. Hal ini wajar terjadi karena mereka yang berada di fase awal karier cenderung lebih dinamis dan aktif berpindah pekerjaan untuk mencari pengalaman baru, kecocokan budaya kerja, atau lonjakan kompensasi, dibandingkan dengan karyawan yang sudah mapan dan mengutamakan stabilitas.

### Rekomendasi Action Items (Optional)

**Optimasi Kompensasi (Monthly Income)**
Karena pendapatan adalah faktor utama, perusahaan perlu memastikan skema penggajian tetap kompetitif tanpa merusak struktur finansial perusahaan.
- Salary Benchmarking: Lakukan riset pasar secara berkala untuk memastikan standar gaji di perusahaan tidak berada di bawah rata-rata industri untuk posisi yang serupa.
- Performance-Based Bonus: Implementasikan sistem bonus atau insentif berbasis kinerja yang transparan. Ini memberikan rasa kendali kepada karyawan atas pendapatan mereka.
- Non-Cash Benefits: Jika kenaikan gaji pokok sulit dilakukan, tawarkan kompensasi dalam bentuk lain seperti tunjangan kesehatan yang lebih luas, subsidi transportasi, atau wellness program.

**Strategi Retensi Karyawan Muda (Age)**
Karyawan muda sering kali mencari pertumbuhan cepat. Jika mereka merasa stagnan, mereka akan pergi.
- Clear Career Pathing: Buat pemetaan karier yang jelas. Karyawan muda perlu melihat "tangga" yang bisa mereka daki dalam 1–3 tahun ke depan.
- Mentorship & Learning: Luncurkan program mentor di mana karyawan senior membimbing karyawan muda. Berikan akses ke kursus sertifikasi atau pelatihan skill baru secara gratis.
- Internal Mobility: Berikan kesempatan bagi karyawan untuk mencoba peran di departemen lain (cross-functional) sebelum mereka memutuskan untuk mencari tantangan di luar perusahaan.

**Program Pengembangan & Keterikatan Awal Karier (Total Working Years)**
Karyawan dengan pengalaman kerja yang masih minim umumnya berada di fase eksplorasi dan lebih rentan berpindah perusahaan (job-hopping). Perusahaan perlu membangun keterikatan dan komitmen mereka sejak awal.
- Milestone Recognition: Berikan apresiasi atau bonus retensi pada tonggak masa kerja tertentu (misalnya, bonus loyalitas setelah 1 atau 2 tahun). Ini memberikan insentif jangka pendek agar mereka menunda keinginan untuk segera pindah.
- Impactful Project Involvement: Karyawan di fase awal karier sangat fokus pada membangun portofolio dan skill. Libatkan mereka dalam proyek strategis agar mereka merasa memberikan dampak nyata dan mendapatkan pengalaman berharga tanpa harus mencari tantangan di perusahaan lain.
- Culture Integration & Buddy System: Perkuat program onboarding yang tidak hanya berfokus pada teknis pekerjaan, tetapi juga integrasi sosial. Pasangkan mereka dengan "buddy" (rekan kerja sebaya) agar mereka lebih cepat beradaptasi, merasa nyaman, dan terhubung secara emosional dengan tim.


### Inference Model
1. Buka file inference_model.py
2. Ubah data sample_employee yang ingin diprediksi
3. Jalankan perintah
```
python inference_model.py
```
