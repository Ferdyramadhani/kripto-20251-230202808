# Laporan Praktikum Kriptografi
Minggu ke-: 2 
Topik: [cryptosystem]  
Nama: [Ferdy Ramadhani]  
NIM: [230202808]  
Kelas: [5IKRA]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Mengidentifikasi komponen dasar kriptosistem (plaintext, ciphertext, kunci, algoritma).  
2. Menggambarkan proses enkripsi dan dekripsi sederhana.  
3. Mengklasifikasikan jenis kriptosistem (simetris dan asimetris).  )

---

## 2. Dasar Teori
Cipher Klasik adalah metode enkripsi historis yang digunakan untuk mengamankan komunikasi sebelum era digital. Teknik ini biasanya hanya melibatkan substitusi (penggantian huruf dengan huruf lain atau simbol, seperti pada Caesar Cipher) atau transposisi (pengubahan urutan huruf, seperti pada Rail Fence Cipher). Cipher klasik beroperasi pada level karakter dan umumnya dieksekusi secara manual. Meskipun saat ini dianggap tidak aman terhadap serangan kriptanalisis modern, konsep dasar yang melibatkan kunci untuk mengubah plaintext menjadi ciphertext merupakan fondasi konseptual dari seluruh bidang kriptografi.

Aritmetika Modular adalah sistem matematika fundamental yang menjadi tulang punggung hampir semua kriptosistem modern, terutama untuk enkripsi kunci publik (Public-Key Cryptography). Konsep ini sering disebut sebagai "aritmetika jam", karena angka akan "berputar" kembali setelah mencapai suatu nilai yang disebut modulus (n). Intinya, operasi a(modn) hanya memberikan sisa dari pembagian a oleh n. Dua bilangan, a dan b, dikatakan kongruen modulo n (a≡b(modn)) jika mereka memiliki sisa yang sama ketika dibagi n. Kerumitan dari operasi ini, terutama ketika melibatkan bilangan prima besar dan eksponensiasi, menciptakan kesulitan komputasi yang menjadi basis keamanan dalam algoritma kunci publik seperti RSA.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
1. Sebutkan komponen utama dalam sebuah kriptosistem.
    - Pesan (Plaintext): Data atau informasi asli yang dapat dibaca dan dimengerti.

    - Ciphertext: Pesan yang telah disandi (encrypted) sehingga tidak dapat dipahami tanpa kunci.

    - Kunci (Key): Parameter rahasia (berupa string atau deretan bilangan) yang digunakan sebagai masukan untuk mengubah plaintext menjadi ciphertext dan sebaliknya.

    - Algoritma Cipher (Cipher): Fungsi atau aturan matematis yang digunakan untuk melakukan proses Enkripsi (mengubah plaintext menjadi ciphertext) dan Dekripsi (mengembalikan ciphertext menjadi plaintext).

    - Pengirim dan Penerima: Dua entitas (orang, komputer, dll.) yang berkomunikasi dan memproses pesan menggunakan kriptosistem.  
2. Apa kelebihan dan kelemahan sistem simetris dibandingkan asimetris? 
    Simetris (Satu Kunci) 
    - Kelebihan :Kecepatan Tinggi: Algoritma (contoh: AES) lebih sederhana, sehingga proses enkripsi dan dekripsi sangat cepat, efisien untuk data bervolume besar.

    - Kekurangan :Masalah Distribusi Kunci: Kunci rahasia harus dibagikan melalui saluran yang aman, yang sulit dicapai dalam komunikasi skala besar.

    Asimetris (Pasangan Kunci)
    - Kelebihan :Memecahkan Masalah Distribusi Kunci: Hanya kunci publik yang perlu dibagikan, sehingga kunci privat tetap aman. Memberikan fungsi otentikasi dan anti-penyangkalan.

    - Kekurangan :Proses Lambat: Algoritma (contoh: RSA) melibatkan operasi matematika yang lebih kompleks (seperti perpangkatan besar), sehingga jauh lebih lambat dan memerlukan daya komputasi lebih besar.
3. Mengapa distribusi kunci menjadi masalah utama dalam kriptografi simetris?
    Distribusi kunci adalah masalah utama dalam kriptografi simetris karena sistem ini menuntut agar kunci yang sama (kunci rahasia) diketahui oleh pengirim dan penerima, dan pada saat yang sama, kunci tersebut harus dirahasiakan dari pihak lain.

    - Risiko Penyadapan: Jika kunci dikirimkan melalui saluran komunikasi yang sama dengan pesan  terenkripsi (atau bahkan saluran lain yang tidak terjamin keamanannya), kunci tersebut berisiko disadap oleh pihak ketiga. Jika kunci berhasil dicuri, keamanan seluruh pesan yang dienkripsi dengan kunci tersebut akan runtuh.

    - Kebutuhan Saluran Aman Independen: Agar komunikasi simetris aman, pengirim dan penerima harus terlebih dahulu sepakat mengenai kunci secara rahasia melalui saluran yang sudah aman (pre-existing secure channel) sebelum komunikasi utama dimulai. Dalam skenario komunikasi yang luas (misalnya, internet), membangun saluran aman yang terpisah untuk setiap pasangan pengguna sangat tidak praktis dan mahal.
---

## 8. Kesimpulan
Kriptosistem, sebagai fondasi keamanan informasi, pada dasarnya adalah seni mengubah data yang dapat dibaca (Plaintext) menjadi data yang tidak dapat dipahami (Ciphertext). Secara historis, dasar ini diletakkan oleh Cipher Klasik (seperti substitusi), namun keamanannya saat ini sepenuhnya bergantung pada matematika, khususnya Aritmetika Modular. Konsep sisa pembagian ini menyediakan kompleksitas komputasi yang esensial, terutama dalam algoritma modern.

Setiap kriptosistem harus memiliki lima komponen utama: Plaintext, Ciphertext, Algoritma Cipher, Kunci, serta entitas Pengirim dan Penerima. Peran kritis dipegang oleh Kunci, yang menentukan jenis kriptosistem dan tantangan keamanannya.
---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit Week2-cryptosytem
Author: Ferdy Ramadhani <ferdyramadhani225@gmail.com>
Date:   2025-10-10

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
