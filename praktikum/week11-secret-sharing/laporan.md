# Laporan Praktikum Kriptografi
Minggu ke-: 11  
Topik: [Secret-sharing]  
Nama: [Ferdy Ramadhani]  
NIM: [230202808]  
Kelas: [5IKRA]  

---

## 1. Tujuan
Tujuan dari praktikum ini adalah:
1. Menjelaskan konsep Shamir Secret Sharing (SSS).
2. Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.
3. Menganalisis keamanan skema distribusi rahasia berbasis threshold.

---

## 2. Dasar Teori
Shamir’s Secret Sharing adalah metode kriptografi untuk membagi sebuah rahasia menjadi beberapa bagian (share), di mana rahasia hanya dapat dipulihkan jika jumlah bagian minimum (threshold) digabungkan. Metode ini meningkatkan keamanan dengan mencegah satu pihak tunggal menguasai seluruh rahasia.

Skema ini menggunakan prinsip interpolasi polinomial, di mana rahasia disimpan sebagai konstanta polinomial. Share yang jumlahnya kurang dari threshold tidak memberikan informasi apa pun tentang rahasia, sedangkan share yang memenuhi threshold dapat merekonstruksi rahasia secara utuh.

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
from secretsharing import SecretSharer

secret_text = "KriptografiUPB2025"

secret_hex = secret_text.encode("utf-8").hex()

# Membagi rahasia menjadi 5 share dengan threshold 3
shares = SecretSharer.split_secret(secret_hex, 3, 5)
print("Shares:", shares)

recovered_hex = SecretSharer.recover_secret(shares[:3])

recovered_text = bytes.fromhex(recovered_hex).decode("utf-8")
print("Recovered secret:", recovered_text)
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
1. Apa keuntungan utama Shamir Secret Sharing dibanding membagikan salinan kunci secara langsung?
   - euntungan utama Shamir’s Secret Sharing dibanding membagikan salinan kunci secara langsung adalah keamanan dan keandalan yang lebih tinggi. Pada pembagian salinan kunci, jika satu salinan bocor maka seluruh kunci langsung terkompromi. Sebaliknya, pada Shamir Secret Sharing, satu atau beberapa share yang bocor tidak mengungkapkan apa pun tentang kunci selama belum mencapai jumlah ambang (threshold).
2. Apa peran threshold (k) dalam keamanan secret sharing?
   - hreshold (k) berperan sebagai batas minimum jumlah share yang harus digabungkan untuk merekonstruksi sebuah rahasia. Jika jumlah share yang tersedia kurang dari k, maka rahasia tidak dapat diketahui sama sekali, sehingga informasi tetap aman meskipun beberapa share bocor.
Dalam konteks keamanan, nilai k menentukan tingkat perlindungan dan toleransi kegagalan. Semakin besar nilai k, semakin sulit bagi pihak tidak berwenang untuk mengakses rahasia, tetapi ketersediaan sistem menjadi lebih rendah. Sebaliknya, nilai k yang lebih kecil meningkatkan kemudahan pemulihan rahasia, namun dengan tingkat keamanan yang lebih rendah.
3. Contoh skenario nyata penggunaan SSS
   - Pengamanan private key cryptocurrency di mana kunci dibagi ke beberapa pemilik, dan hanya kombinasi tertentu yang dapat melakukan transaksi.
---

## 8. Kesimpulan
Berdasarkan praktikum yang telah dilakukan, Shamir Secret Sharing (SSS) terbukti mampu membagi dan merekonstruksi rahasia secara aman menggunakan mekanisme threshold. Hasil percobaan menunjukkan bahwa rahasia hanya dapat dipulihkan ketika jumlah share yang digunakan memenuhi nilai ambang yang ditentukan.

Skema ini efektif meningkatkan keamanan distribusi kunci karena kebocoran satu atau beberapa share tidak mengungkapkan informasi rahasia. Dengan demikian, Shamir Secret Sharing cocok diterapkan pada sistem yang membutuhkan keamanan tinggi, keandalan, dan toleransi kegagalan dalam pengelolaan rahasia.

---

## 9. Daftar Pustaka
- Hineman, A., & Blaum, M. (2022).
- Malinda, D. N., Kusyanti, A., & Bakhtiar, F. A. (2022).
---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit week11-secret-sharing
Author: Ferdy Ramadhani <ferdyramadhani225@gmail.com>
Date:   2025-12-27

    week11-secret-sharing: implementasi dan laporan Shamir Secret Sharing
```
