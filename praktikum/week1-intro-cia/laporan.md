# Laporan Praktikum Kriptografi
Minggu ke-: 1  
Topik: [Ringkasan Sejarah dan Quiz]  
Nama: [Ferdy Ramadhani]  
NIM: [230202808]  
Kelas: [5IKRA]  

---

## 1. Ringkasan sejarah kriptografi
Kriptografi merupakan salah satu cabang ilmu yang berhubungan dengan keamanan informasi. Istilah ini berasal dari bahasa Yunani, yaitu kryptos yang berarti “rahasia” dan graphein yang berarti “menulis”. Secara sederhana, kriptografi dapat diartikan sebagai seni dan ilmu untuk menyembunyikan pesan agar hanya dapat dibaca oleh pihak yang berhak.

Sejarah kriptografi dimulai sejak zaman kuno. Pada masa itu, kriptografi digunakan untuk kepentingan militer dan diplomatik, agar pesan penting tidak diketahui oleh musuh. Salah satu contoh paling terkenal adalah Caesar Cipher, yang digunakan oleh Julius Caesar untuk mengirimkan pesan rahasia kepada panglima perangnya. Teknik ini bekerja dengan cara menggeser huruf-huruf dalam alfabet sejumlah langkah tertentu. Misalnya, huruf A digeser menjadi D jika digeser tiga langkah. Walaupun sederhana, pada masanya teknik ini sangat efektif untuk menjaga kerahasiaan informasi.

Memasuki abad pertengahan, kriptografi mulai berkembang lebih kompleks. Banyak kerajaan menggunakan berbagai metode substitusi dan transposisi untuk mengenkripsi pesan. Namun, kelemahannya adalah jika seseorang mengetahui pola atau kunci yang digunakan, pesan tersebut dapat dengan mudah dibongkar.

Perkembangan pesat terjadi pada era perang dunia. Saat Perang Dunia II, Jerman menggunakan mesin Enigma untuk mengamankan komunikasi militernya. Mesin ini mampu menghasilkan kode yang sangat rumit dan sulit dipecahkan. Namun, upaya besar-besaran yang dilakukan oleh tim sekutu di bawah pimpinan Alan Turing akhirnya berhasil memecahkan kode tersebut. Keberhasilan ini bukan hanya membantu memenangkan perang, tetapi juga menjadi dasar lahirnya komputer modern dan sistem kriptografi baru.

Seiring berkembangnya teknologi komputer pada pertengahan abad ke-20, kriptografi mulai berubah dari teknik manual menjadi berbasis algoritma matematika. Pada tahun 1970-an muncul DES (Data Encryption Standard) sebagai standar enkripsi pertama yang digunakan secara luas. Kemudian pada tahun 1977, diperkenalkan algoritma RSA (Rivest–Shamir–Adleman) yang menggunakan bilangan prima besar sebagai kunci, dan menjadi dasar dari sistem kriptografi modern.

Memasuki era digital dan internet, kriptografi memainkan peran yang jauh lebih besar. Kini, kriptografi tidak hanya digunakan untuk menyembunyikan pesan, tetapi juga untuk melindungi data digital, seperti transaksi online, komunikasi melalui aplikasi pesan, tanda tangan digital, hingga sistem cryptocurrency seperti Bitcoin yang menggunakan prinsip kriptografi kunci publik.

Dari masa ke masa, kriptografi terus berevolusi seiring kemajuan teknologi dan kebutuhan keamanan informasi. Dapat disimpulkan bahwa kriptografi telah berkembang dari sekadar alat penyamaran pesan di zaman kuno menjadi pondasi utama keamanan data di era digital saat ini. Tanpa kriptografi, dunia modern yang serba online ini akan jauh lebih rentan terhadap ancaman dan kebocoran informasi.
## 2. Prinsip CIA
- Confidentiality (Kerahasiaan) berarti menjaga agar informasi hanya dapat diakses oleh pihak yang berwenang. Contoh nyata:Penggunaan password atau enkripsi pada akun email agar hanya pemiliknya yang bisa membaca isi pesan. Misalnya, ketika Anda login ke Gmail, data dikirim melalui HTTPS (Secure Protocol) untuk menjaga kerahasiaan informasi dari penyadapan.
- Integrity (Integritas) menekankan bahwa data harus tetap asli dan tidak berubah dari bentuk semula. Artinya, informasi tidak boleh dimodifikasi tanpa izin. Untuk menjaga integritas, digunakan teknik seperti hashing dan tanda tangan digital.contoh nyata:Saat Anda melakukan transfer uang melalui mobile banking, sistem memastikan jumlah uang yang dikirim dan diterima tetap sama, tanpa diubah oleh pihak ketiga. Penggunaan checksum atau digital signature juga membantu menjaga integritas data.
- Availability (Ketersediaan) memastikan bahwa informasi dan sistem selalu dapat diakses kapan pun oleh pengguna yang berhak. Misalnya dengan backup data, server cadangan, atau perlindungan dari serangan DDoS agar layanan tidak down.contoh nyata:Situs perbankan online harus selalu bisa diakses nasabah untuk transaksi kapan saja. Untuk itu, bank menggunakan server cadangan (backup server) dan sistem keamanan terhadap serangan DDoS agar layanan tetap aktif.
## 3. Quiz Singkat
1. Siapa tokoh yang dianggap sebagai bapak kriptografi modern?
Whitfield Diffie dan Martin Hellman.
2. Sebutkan algoritma kunci publik yang populer digunakan saat ini.
- RSA (Rivest–Shamir–Adleman)
- Diffie–Hellman (DH)
- DSA (Digital Signature Algorithm)
- ECC (Elliptic Curve Cryptography)
- ElGamal
3. Apa perbedaan utama antara kriptografi klasik dan kriptografi modern?
- Pertama, dari dasar pengamanan, kriptografi klasik menggunakan teknik sederhana seperti substitusi dan transposisi huruf, sedangkan kriptografi modern memakai algoritma matematika kompleks untuk melindungi data digital.

- Kedua, dari jenis kunci, kriptografi klasik menggunakan satu kunci (symmetric key) untuk enkripsi dan dekripsi, sementara kriptografi modern menggunakan dua kunci (asymmetric key), yaitu kunci publik dan kunci privat.

- Ketiga, berdasarkan media dan tujuan, kriptografi klasik digunakan untuk pesan teks sederhana, sedangkan kriptografi modern digunakan dalam keamanan data digital seperti transaksi online dan komunikasi internet.

- Keempat, dari segi keamanan, kriptografi klasik mudah dipecahkan, sedangkan kriptografi modern jauh lebih kuat karena didukung oleh komputasi dan matematika tingkat tinggi.
## 4. Commit Log
commit week1-intro-cia
Author: Ferdy Ramadhani <ferdyramadhani225@gmail.com>
Date:   2025-10-05