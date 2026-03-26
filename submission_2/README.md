# Proyek Akhir: Menyelesaikan Permasalahan Jaya Jaya Institut

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik.

### Permasalahan Bisnis
Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Cakupan Proyek
- Mengamati dataset siswa yang dimiliki Jaya Jaya Institut
- Melakukan exploratory data siswa, dan mencoba menemukan informasi menarik yang dapat menyelesaikan permasalahan
- Melakukan pembersihan data siswa
- Membuat sebuah model machine learning yang dapat digunakan untuk memprediksi kemungkinan seorang siswa akan dropout berdasarkan parameter yang berkorelasi
- Melakukan evaluasi dari model machine learning tersebut
- Menemukan parameter apa saja yang mempengaruhi seorang siswa dropout
- Membuat model inference dalam bentuk web based menggunakan streamlit
- Membuat business dashboard berbasis metabase

### Persiapan

Sumber data: data.csv (https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment notebook:

```
pip install -r requirements.txt
```

Setup metabase:

```
docker build -t metabase-image .
docker run -d -p 3000:3000 --name metabase metabase-image
```

Link Web Streamlit:
https://dicoding-expert-data-science-aminullohzaqi.streamlit.app/

Metabase credentials:
Username: root@mail.com
Password: root123

## Business Dashboard
Pembuatan business dashboard telah menggunakan prinsip design dan integritas. Grafik yang tertera sudah ditentukan berdasarkan parameter yang paling krusial terhadap permasalahan yang dialami. Tata letak dari dashboard sudah sesuai dengan sweet spot, dan diurutkan berdasarkan parameter yang paling berpengaruh.

Dashboard terdiri dari:
1. Jumlah siswa secara keseluruhan
2. Dropout rate
3. Jumlah siswa pemegang beasiswa
4. Status siswa berdasarkan admission grade
5. Status siswa berdasarkan previous qualification grade
6. Perbandingan nilai semester 1 dan 2 terhadap dropout
7. Status siswa berdasarkan usia saat mendaftar
8. Status siswa berdasarkan gender

## Menjalankan Sistem Machine Learning
Cara menjalankan inferece model web based (streamlit):
```
streamlit run app.py
```

## Conclusion

**Kualitas Dataset**
- Dataset yang digunakan tidak memiliki null values
- Dataset tidak terdapat duplikasi data
- Dataset terdapat outlier dalam beberapa kolom numerik. Akan tetapi, value yang dianggap outlier sangatlah wajar dikarenakan value tersebut benar adanya. Sebagai contoh terdapat beberapa outlier pada kolom Age_at_enrollment yang besarannya tinggi. Hal tersebut adalah wajar karena siswa yang mendapat usia tersebut adalah siswa yang memiliki usia lebih dari 50 tahun, sehingga sangatlah berbeda dengan siswa yang lainnya. Keputusan untuk tidak menghapus outlier adalah karena data tersebut benar adanya, dan bukan merupakan kesalahan sistem.

**Model Performance**
Model XGBoost berhasil memprediksi mahasiswa yang dropout dengan akurasi keseluruhan yang cukup baik sebesar 87% dan dengan F1 sebesar 0.79 untuk kelas minoritas "Dropout". Ini membuktikan bahwa tingkat dropout mahasiswa bukanlah sesuatu yang random dan hal ini sangat bisa diprediksi berdasarkan indikator-indikator awal.

Link sreamlit website: https://dicoding-expert-data-science-aminullohzaqi.streamlit.app/

**Interpretasi Faktor Utama Mahasiswa Putus Kuliah (Dropout)**
Berdasarkan hasil pemodelan menggunakan XGBoost dan analisis pentingnya fitur (feature importance), berikut adalah tiga kelompok faktor utama yang paling signifikan mempengaruhi kemungkinan mahasiswa untuk meninggalkan institusi:

1. Admission Grade & Previous Qualification (Nilai Masuk dan Kualifikasi Sebelumnya):
Rekam jejak akademik sebelum masuk ke perguruan tinggi turut menjadi penentu tingkat kesiapan mahasiswa. Mahasiswa dengan nilai pendaftaran atau kualifikasi masa lalu yang lebih rendah umumnya memiliki risiko dropout yang lebih tinggi. Hal ini menunjukkan bahwa kesiapan fondasi keilmuan di awal sangat memengaruhi kemampuan mahasiswa dalam beradaptasi dengan lonjakan beban dan tingkat kesulitan (rigor) materi di jenjang pendidikan tinggi.
2. Curricular Units Approved & Grade (Tingkat Kelulusan SKS dan Nilai Semester Awal):
Merupakan faktor dengan skor kepentingan tertinggi. Mahasiswa yang gagal menyelesaikan banyak mata kuliah atau mendapatkan nilai yang rendah pada semester 1 dan 2 memiliki risiko dropout yang jauh lebih tinggi. Hal ini menunjukkan bahwa performa dan momentum akademik di tahun pertama kuliah adalah indikator paling krusial untuk memprediksi keberhasilan studi.
3. Age at Enrollment (Usia Saat Mendaftar):
Usia menunjukkan pengaruh yang signifikan terhadap tingkat dropout. Mahasiswa yang mendaftar pada usia yang lebih tua (mahasiswa non-tradisional) cenderung memiliki tingkat putus kuliah yang lebih tinggi. Hal ini wajar terjadi karena mereka umumnya memiliki tanggung jawab eksternal yang lebih besar, seperti pekerjaan atau keluarga, yang membuat mereka lebih rentan terhadap tekanan komitmen waktu dibandingkan mahasiswa reguler yang baru lulus dari sekolah menengah.


### Rekomendasi Action Items
Berdasarkan features dominan pendorong dropout, berikut adalah langkah-langkah nyata yang harus diambil institusi untuk meminimalisir jumlah mahasiswa dropout:

**Terapkan Sistem Peringatan Dini (Early Warning System) di Semester 1**
- Data: Features seperti curricular_units_1st_sem_approved dan curricular_units_1st_sem_grade adalah prediktor utama.
- Tindakan: Jangan menunggu sampai akhir tahun ajaran untuk turun tangan. Institusi harus melacak nilai Ujian Tengah Semester (UTS) dan kegagalan tugas sejak awal semester 1. Jika seorang mahasiswa terdeteksi "berisiko" tidak lulus mata kuliahnya, segera picu sistem agar pembimbing akademik (Dosen Wali) atau tutor sebaya langsung menghubungi mereka.

**Manajemen Beban Kuliah Proaktif**
- Data: Jumlah SKS yang diambil maupun yang lulus di seluruh semester adalah pendorong yang sangat besar.
- Tindakan: Mahasiswa yang mengambil beban SKS penuh tetapi gagal lulus berisiko tinggi mengalami burnout dan putus kuliah. Pembimbing akademik harus menggunakan dashboard yang kita bahas sebelumnya untuk mendeteksi mahasiswa yang mengambil beban di luar kemampuan mereka. Terapkan kebijakan yang membatasi pengambilan SKS maksimal di semester 2 jika tingkat kelulusan di semester 1 terlalu rendah.

**Buat Program Matrikulasi/Pendampingan untuk Mahasiswa Baru Berisiko**
- Data: admission_grade dan previous_qualification_grade menunjukkan bahwa kesiapan akademik dasar sangatlah penting.
- Tindakan: Identifikasi mahasiswa baru dengan nilai ujian masuk atau kualifikasi sebelumnya yang lebih rendah sebelum perkuliahan dimulai. Wajibkan mereka mengikuti program pendampingan atau matrikulasi yang berfokus pada keterampilan belajar, manajemen waktu, dan pengetahuan dasar untuk memastikan mereka siap menghadapi kerasnya dunia perkuliahan.

**Dukungan Khusus untuk Demografi Non-Tradisional & Rentan**
- Data: age_at_enrollment dan Gender masuk dalam 10 besar pendorong dropout.
- Tindakan: Mahasiswa yang lebih tua (yang seringkali harus membagi waktu antara pekerjaan, keluarga, dan kuliah) kemungkinan menghadapi tekanan yang berbeda dibandingkan mahasiswa baru yang masih berusia 18 tahun. Buat struktur dukungan yang fleksibel, seperti bimbingan di malam hari atau sesi advising asinkron. Selain itu, selidiki kesenjangan gender dalam tingkat dropout melalui survei kualitatif untuk melihat apakah program mentorship khusus dapat membantu mengatasi masalah tersebut.

**Beralih dari Analitik Evaluasi Akhir ("Post-Mortem") ke Preventif**
- Data: Model yang telah dibentuk sudah cukup akurat.
- Tindakan: Terapkan (deploy) model XGBoost ini ke tahap produksi. Masukkan data mahasiswa yang berstatus aktif saat ini ke dalam model pada minggu ke-4, ke-8, dan ke-12 di setiap semester untuk menghasilkan "Skor Risiko" (Risk Score) secara real-time bagi setiap mahasiswa. Berikan daftar prediksi ini langsung kepada departemen bimbingan konseling dan pimpinan program studi.
