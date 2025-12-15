# Laporan Praktikum Kriptografi
Minggu ke-: 10  
Topik: [Public Key Infrastructure (PKI & Certificate Authority)]  
Nama: [Ferdy Ramadhani]  
NIM: [230202808]  
Kelas: [5IKRA]  

---

## 1. Tujuan
1. Membuat sertifikat digital sederhana.
2. Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.
3. Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS).

---

## 2. Dasar Teori
Public Key Infrastructure (PKI) adalah kerangka kerja keamanan yang digunakan untuk mengelola kunci kriptografi berbasis kunci publik dan privat guna menjamin kerahasiaan, integritas, autentikasi, dan non-repudiation dalam komunikasi digital. PKI memanfaatkan kriptografi kunci publik, di mana setiap entitas memiliki sepasang kunci: public key yang dapat dibagikan dan private key yang dijaga kerahasiaannya. Infrastruktur ini banyak diterapkan pada layanan keamanan seperti SSL/TLS, tanda tangan digital, dan enkripsi email.

Certificate Authority (CA) merupakan komponen utama dalam PKI yang berperan sebagai pihak tepercaya untuk menerbitkan dan memverifikasi sertifikat digital. Sertifikat digital mengikat identitas pemilik (individu, organisasi, atau server) dengan public key tertentu, sehingga pihak lain dapat memastikan keaslian identitas tersebut. Selain menerbitkan sertifikat, CA juga bertanggung jawab dalam pengelolaan masa berlaku, pencabutan sertifikat (melalui CRL atau OCSP), serta menjaga kepercayaan dalam ekosistem PKI.
Dengan adanya PKI dan CA, proses pertukaran data melalui jaringan terbuka seperti internet dapat dilakukan secara aman karena identitas pihak yang berkomunikasi dapat diverifikasi dan data terlindungi dari penyadapan maupun pemalsuan. Oleh karena itu, PKI menjadi fondasi penting dalam sistem keamanan informasi modern, khususnya pada aplikasi berbasis web, e-commerce, dan sistem pemerintahan elektronik.

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
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta

# Generate key pair
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Buat subject & issuer (CA sederhana = self-signed)
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UPB Kriptografi"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"example.com"),
])

# Buat sertifikat
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.utcnow())
    .not_valid_after(datetime.utcnow() + timedelta(days=365))
    .sign(key, hashes.SHA256())
)

# Simpan sertifikat
with open("cert.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("Sertifikat digital berhasil dibuat: cert.pem")

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
1. Apa fungsi utama Certificate Authority (CA)?
- Fungsi utama Certificate Authority (CA) adalah menerbitkan dan memverifikasi sertifikat digital yang menghubungkan identitas suatu entitas (pengguna, organisasi, atau server) dengan public key miliknya. Dengan demikian, CA bertindak sebagai pihak tepercaya yang menjamin keaslian identitas dalam komunikasi digital.
Selain itu, CA juga berfungsi untuk mengelola siklus hidup sertifikat digital, termasuk validasi identitas sebelum penerbitan, perpanjangan masa berlaku, serta pencabutan sertifikat jika sertifikat sudah tidak valid atau terjadi kompromi keamanan.
2. Mengapa self-signed certificate tidak cukup untuk sistem produksi?
- Self-signed certificate tidak cukup untuk sistem produksi karena tidak memiliki kepercayaan dari pihak ketiga. Sertifikat ini ditandatangani oleh pemiliknya sendiri, sehingga identitas server atau aplikasi tidak dapat diverifikasi secara independen. Akibatnya, browser dan klien akan menampilkan peringatan keamanan karena sertifikat tidak berasal dari Certificate Authority (CA) tepercaya.
Selain itu, self-signed certificate tidak cocok untuk lingkungan dengan banyak pengguna karena pengelolaan kepercayaannya tidak terpusat. Setiap klien harus secara manual mempercayai sertifikat tersebut, yang berisiko menimbulkan kesalahan konfigurasi dan membuka peluang serangan seperti man-in-the-middle.
3. Bagaimana PKI mencegah serangan MITM dalam komunikasi TLS/HTTPS?
- PKI mencegah serangan Man-in-the-Middle (MITM) pada komunikasi TLS/HTTPS dengan memastikan keaslian identitas server melalui sertifikat digital yang diterbitkan oleh Certificate Authority (CA) tepercaya. Saat klien (misalnya browser) mengakses situs HTTPS, server mengirimkan sertifikat digital yang berisi public key dan identitasnya. Klien kemudian memverifikasi sertifikat tersebut dengan root certificate CA yang sudah tersimpan di sistem. Jika sertifikat valid dan sesuai dengan domain, klien dapat yakin bahwa ia benar-benar berkomunikasi dengan server yang sah, bukan penyerang.
Selain autentikasi, PKI juga menjamin integritas proses pertukaran kunci. Dalam TLS handshake, public key pada sertifikat digunakan untuk mengamankan pembentukan session key simetris. Karena hanya server yang memiliki private key yang sesuai, penyerang tidak dapat menyamar atau membaca kunci sesi meskipun berada di tengah komunikasi.
---

## 8. Kesimpulan
Berdasarkan praktikum yang telah dilakukan, dapat disimpulkan bahwa Public Key Infrastructure (PKI) berperan penting dalam menjamin keamanan komunikasi digital melalui pengelolaan kunci kriptografi dan sertifikat digital. Pembuatan sertifikat digital sederhana menunjukkan bagaimana identitas dan public key dapat diikat secara kriptografis untuk mendukung proses autentikasi.

Selain itu, Certificate Authority (CA) terbukti memiliki peran sentral sebagai pihak tepercaya dalam penerbitan dan validasi sertifikat digital. Melalui mekanisme ini, PKI mampu mencegah ancaman keamanan seperti Man-in-the-Middle (MITM) pada komunikasi TLS/HTTPS dengan memastikan keaslian identitas dan integritas pertukaran kunci. Dengan demikian, PKI menjadi fondasi utama dalam penerapan sistem keamanan informasi modern.

---

## 9. Daftar Pustaka
- Wathoni, M., Nurhasanah, R., Shela, D., Informasi, P. T., Pendidikan, F. I., Muhammadiyah, U., & Selatan, K. T. (n.d.). Penerapan konfigurasi dasar pki dua tingkat: active directory certificate services (ad cs). 55–62.

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit week-pki
Author: Ferdy Ramadhani <ferdyramadhani225@gamil.com>
Date:   2025-09-20

    week10-pki: Public Key Infrastructure (PKI & Certificate Authority)
```
