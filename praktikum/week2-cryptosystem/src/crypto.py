def enkripsi_caesar(plaintext, shift):
    hasil = ""
    for char in plaintext:
        if char.isalpha():  # hanya huruf yang dienkripsi
            # tentukan base (A atau a)
            base = ord('A') if char.isupper() else ord('a')
            # geser huruf sesuai shift
            hasil += chr((ord(char) - base + shift) % 26 + base)
        else:
            hasil += char  # karakter non-huruf tidak diubah
    return hasil


def dekripsi_caesar(ciphertext, shift):
    # cukup panggil fungsi enkripsi dengan pergeseran negatif
    return enkripsi_caesar(ciphertext, -shift)


# ---- Program Utama ----
if __name__ == "__main__":
    teks_asli = input("Masukkan teks asli (plaintext): ")
    kunci = int(input("Masukkan nilai pergeseran (key): "))

    cipher = enkripsi_caesar(teks_asli, kunci)
    print("\nHasil Enkripsi  :", cipher)

    hasil_dekripsi = dekripsi_caesar(cipher, kunci)
    print("Hasil Dekripsi  :", hasil_dekripsi)
