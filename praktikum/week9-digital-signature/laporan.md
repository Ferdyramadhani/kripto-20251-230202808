# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: [Digital Signature]  
Nama: [Ferdy Ramadhani]  
NIM: [230202808]  
Kelas: [5IKRA]  

---

## 1. Tujuan
- Mengimplementasikan tanda tangan digital menggunakan algoritma RSA/DSA.
- Memverifikasi keaslian tanda tangan digital.
- Menjelaskan manfaat tanda tangan digital dalam otentikasi pesan dan integritas data.(Tuliskan tujuan pembelajaran praktikum sesuai modul.)

---

## 2. Dasar Teori
Digital signature atau tanda tangan digital adalah mekanisme kriptografi yang digunakan untuk menjamin keaslian, integritas, dan non-repudiation sebuah pesan atau dokumen elektronik. Teknologi ini bekerja menggunakan kriptografi kunci publik (public key cryptography), yaitu sepasang kunci: private key untuk membuat tanda tangan dan public key untuk memverifikasinya.

Prosesnya dimulai dengan membangkitkan hash dari pesan menggunakan algoritma hash seperti SHA-256. Hash ini bersifat unik sehingga perubahan sekecil apa pun pada pesan akan menghasilkan nilai hash berbeda. Nilai hash tersebut kemudian dienkripsi menggunakan private key pengirim sehingga terbentuklah digital signature. Ketika penerima menerima pesan, ia akan menghitung kembali hash pesan, kemudian mendekripsi tanda tangan menggunakan public key pengirim. Jika kedua hash sama, berarti pesan benar-benar asli, tidak berubah, dan memang berasal dari pemilik private key.

Dengan cara ini, digital signature memberikan jaminan bahwa pesan tidak dimodifikasi (integrity), benar-benar dikirim oleh pihak yang mengklaim mengirim (authentication), dan pengirim tidak dapat menyangkal bahwa ia pernah mengirim pesan tersebut (non-repudiation).)

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
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate pasangan kunci RSA
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Pesan yang akan ditandatangani
message = b"Hello, ini pesan penting."
h = SHA256.new(message)

# Buat tanda tangan dengan private key
signature = pkcs1_15.new(private_key).sign(h)
print("Signature:", signature.hex())

try:
    pkcs1_15.new(public_key).verify(h, signature)
    print("Verifikasi berhasil: tanda tangan valid.")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak valid.")
    
    # Modifikasi pesan
fake_message = b"Hello, ini pesan palsu."
h_fake = SHA256.new(fake_message)

try:
    pkcs1_15.new(public_key).verify(h_fake, signature)
    print("Verifikasi berhasil (seharusnya gagal).")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak cocok dengan pesan.")
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
1. Apa perbedaan utama antara enkripsi RSA dan tanda tangan digital RSA?
   Enkripsi RSA dan tanda tangan digital RSA merupakan dua mekanisme penting dalam kriptografi kunci publik, namun keduanya memiliki fungsi dan alur kerja yang berbeda. Enkripsi RSA digunakan untuk menjaga kerahasiaan informasi. Pada proses ini, pengirim mengenkripsi pesan menggunakan public key milik penerima sehingga pesan tersebut hanya dapat dibuka oleh penerima dengan private key yang ia miliki. Dengan demikian, enkripsi RSA memastikan bahwa pesan tetap rahasia dan tidak dapat diakses oleh pihak yang tidak berwenang.
Sementara itu, tanda tangan digital RSA digunakan untuk memverifikasi identitas pengirim sekaligus memastikan integritas pesan. Pengirim akan membuat hash dari pesan, kemudian menandatanganinya menggunakan private key miliknya. Penerima dapat memverifikasi tanda tangan tersebut menggunakan public key pengirim. Jika hasil verifikasi sesuai, penerima memperoleh kepastian bahwa pesan benar-benar dikirim oleh pengirim yang sah, tidak dimodifikasi selama proses transmisi, serta pengirim tidak dapat menyangkal keterlibatannya dalam pengiriman pesan tersebut (non-repudiation).
Dengan demikian, perbedaan utama keduanya terletak pada tujuan dan arah penggunaan kunci. Enkripsi RSA fokus pada kerahasiaan data, sedangkan tanda tangan digital RSA fokus pada keaslian dan integritas data.
2. Mengapa tanda tangan digital menjamin integritas dan otentikasi pesan?
   Tanda tangan digital menjamin integritas karena sebelum ditandatangani, pesan dibuatkan nilai hash yang unik. Jika pesan berubah sedikit saja, nilai hash juga akan berubah, sehingga verifikasi tanda tangan akan gagal.
Tanda tangan digital juga menjamin otentikasi karena hanya pemilik private key yang dapat membuat tanda tangan tersebut. Penerima dapat memverifikasinya menggunakan public key pengirim, sehingga ia yakin bahwa pesan benar-benar berasal dari pengirim yang sah.
3. Bagaimana peran Certificate Authority (CA) dalam sistem tanda tangan digital modern?
   Certificate Authority (CA) berperan sebagai pihak ketiga tepercaya yang bertugas memverifikasi identitas seseorang atau organisasi sebelum menerbitkan sertifikat digital. Sertifikat digital ini menghubungkan public key dengan identitas pemiliknya, sehingga penerima dapat yakin bahwa public key tersebut memang milik orang atau pihak yang benar.
Dalam sistem tanda tangan digital, CA memastikan bahwa tanda tangan benar-benar berasal dari pemilik private key yang sah. Tanpa CA, siapa pun dapat mengaku memiliki public key tertentu, sehingga proses otentikasi menjadi tidak dapat dipercaya.
Dengan kata lain, CA membuat sistem tanda tangan digital menjadi aman, tepercaya, dan dapat diverifikasi secara publik, terutama dalam komunikasi internet seperti HTTPS, dokumen PDF bertanda tangan digital, dan transaksi elektronik.
)
---

## 8. Kesimpulan
Berdasarkan percobaan, tanda tangan digital berhasil dibuat dan diverifikasi menggunakan algoritma RSA, menunjukkan bahwa mekanisme ini efektif dalam memastikan integritas dan keaslian pesan. Proses verifikasi yang gagal ketika pesan dimodifikasi membuktikan bahwa digital signature mampu mendeteksi perubahan sekecil apa pun pada data. Selain itu, peran Certificate Authority semakin menegaskan pentingnya otentikasi kunci publik dalam sistem tanda tangan digital modern, sehingga komunikasi digital dapat dilakukan secara aman dan tepercaya.

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
