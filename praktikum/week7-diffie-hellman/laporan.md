# Laporan Praktikum Kriptografi
Minggu ke-: 7 
Topik: [Diffiw Hellman]  
Nama: [Ferdy Ramadhani]  
NIM: [230202808]  
Kelas: [5IKRA]  

---

## 1. Tujuan
1. Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.
2. Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
3. Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).

---

## 2. Dasar Teori
Protokol Diffie–Hellman adalah sebuah metode dalam kriptografi modern yang digunakan untuk melakukan key exchange atau pertukaran kunci secara aman melalui kanal komunikasi yang tidak aman. Protokol ini memungkinkan dua pihak yang belum pernah bertemu sebelumnya untuk menghasilkan sebuah kunci rahasia bersama (shared secret key) tanpa harus mengirimkan kunci tersebut secara langsung. Kunci rahasia ini nantinya digunakan untuk enkripsi simetris sehingga komunikasi menjadi aman.

Protokol Diffie–Hellman bekerja berdasarkan konsep matematika bilangan prima dan logaritma diskrit. Dua pihak terlebih dahulu menyepakati dua nilai publik, yaitu bilangan prima besar (p) dan generator (g). Masing-masing pihak kemudian memilih bilangan rahasia (private key), menghitung nilai publiknya, lalu saling menukarnya. Melalui operasi eksponensial modulo (p), kedua pihak dapat menghitung kunci bersama yang identik, sementara pihak luar sangat sulit menghitungnya karena harus memecahkan masalah logaritma diskrit yang secara komputasional sangat sulit.

Keamanan Diffie–Hellman sangat bergantung pada ukuran bilangan prima yang digunakan dan kerahasiaan kunci privat masing-masing pihak. Meskipun aman terhadap penyadapan pasif, protokol ini rentan terhadap serangan man-in-the-middle bila tidak disertai mekanisme autentikasi tambahan seperti sertifikat digital atau tanda tangan digital.

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

```python
import random

# parameter umum (disepakati publik)
p = 23  # bilangan prima
g = 5   # generator

# private key masing-masing pihak
a = random.randint(1, p-1)  # secret Alice
b = random.randint(1, p-1)  # secret Bob

# public key
A = pow(g, a, p)
B = pow(g, b, p)

# exchange public key
shared_secret_A = pow(B, a, p)
shared_secret_B = pow(A, b, p)

print("Kunci bersama Alice :", shared_secret_A)
print("Kunci bersama Bob   :", shared_secret_B)
```


---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/outputt.png)
![Hasil Input](screenshots/inputt.png)
![Hasil Output](screenshots/outputt.png)
)

---

## 7. Jawaban Pertanyaan
1. Mengapa Diffie-Hellman memungkinkan pertukaran kunci di saluran publik?
    - Diffie–Hellman memungkinkan pertukaran kunci melalui saluran publik karena metode ini tidak pernah mengirimkan kunci rahasia secara langsung. Yang dikirimkan hanyalah nilai publik yang sudah dibuat dari kunci privat melalui proses matematika (eksponensial modulo bilangan prima). Nilai publik tersebut tidak dapat dibalik untuk menemukan kunci privat karena memecahkan logaritma diskrit adalah masalah yang sangat sulit dan membutuhkan komputasi besar.
    Selain itu, kedua pihak dapat menghasilkan shared secret key yang sama dengan cara menghitung menggunakan nilai publik lawan dan kunci privat mereka masing-masing. Meskipun penyadap melihat semua nilai publik yang ditransmisikan, ia tidak bisa menghitung kunci rahasia bersama tanpa mengetahui kunci privat peserta. Inilah alasan protokol Diffie–Hellman dapat bekerja aman meskipun seluruh proses pertukaran dilakukan di jaringan yang sepenuhnya terbuka.
2. Apa kelemahan utama protokol Diffie-Hellman murni?
   - Kelemahan utama dari protokol Diffie–Hellman murni (tanpa autentikasi) adalah kerentanannya terhadap serangan Man-in-the-Middle (MitM). Dalam protokol DH asli, kedua pihak hanya bertukar nilai publik tanpa ada mekanisme untuk memverifikasi identitas satu sama lain. Akibatnya, penyerang dapat menyusup di tengah komunikasi, mengganti nilai publik yang dipertukarkan, dan membuat dua shared secret key berbeda dengan masing-masing pihak. Kedua pihak akan mengira mereka berkomunikasi langsung, padahal semua pesan telah dibaca, dimodifikasi, atau diteruskan oleh penyerang.Selain kerentanan MitM, protokol DH murni juga memiliki kelemahan lain seperti ketergantungan pada bilangan prima besar untuk keamanan, tidak menyediakan autentikasi, dan tidak melindungi dari serangan replay tanpa mekanisme tambahan. Namun, yang paling kritis tetap serangan Man-in-the-Middle, karena dapat sepenuhnya membatalkan keamanan pertukaran kunci.
3. Bagaimana cara mencegah serangan MITM pada protokol ini?
   - Untuk mencegah serangan Man-in-the-Middle, protokol Diffie–Hellman perlu diberi autentikasi tambahan. Cara yang paling umum adalah menandatangani nilai publik DH dengan tanda tangan digital, sehingga pihak lain dapat memverifikasi bahwa nilai tersebut asli dan tidak dimodifikasi. Selain itu, penggunaan sertifikat digital dari otoritas terpercaya juga memastikan identitas kedua pihak. Pada protokol modern seperti TLS, digunakan varian Authenticated Diffie–Hellman yang memadukan pertukaran kunci DH dengan autentikasi, sehingga prosesnya tetap aman meskipun dilakukan di saluran publik.
)
---

## 8. Kesimpulan
Berdasarkan percobaan yang dilakukan, protokol Diffie–Hellman berhasil menunjukkan bagaimana dua pihak dapat menghasilkan sebuah shared secret key yang sama meskipun bertukar informasi melalui saluran publik. Simulasi program juga menunjukkan bahwa nilai kunci bersama yang dihasilkan Alice dan Bob identik, sehingga mekanisme pertukaran kunci berjalan sesuai teori. Namun, percobaan ini juga menegaskan bahwa Diffie–Hellman murni masih rentan terhadap serangan Man-in-the-Middle, sehingga diperlukan penambahan autentikasi agar proses pertukaran kunci benar-benar aman.

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
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
