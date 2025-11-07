import random


def angka_acak():
    range_angka = random.randint(1, 15)
    return range_angka


def tebak_angka():
    angka_random = angka_acak()
    percobaan = 3
    print("selamat datang di permainan tebak angka!")
    print("Saya telah memilih sebuah angka antara 1 hingga 15.")
    print(f"Kamu memiliki {percobaan} kesempatan untuk menebaknya.")

    while percobaan > 0:
        try:
            tebakan = int(input("masukan tebakanmu: "))
        except ValueError:
            print("Tolong masukkan angka yang valid.")
            continue

        if tebakan < 1 or tebakan > 15:
            print("Tebakan harus antara 1 hingga 15.")
            continue

        if tebakan == angka_random:
            print("Selamat! Tebakanmu benar!")
            break
        else:
            percobaan -= 1
            if percobaan > 0:
                print(f"Tebakanmu salah. Coba lagi! Sisa percobaan: {percobaan}")
            else:
                print(
                    f"Maaf, kamu kehabisan percobaan. Angka yang benar adalah {angka_random}."
                )
    print("Terima kasih telah bermain!")


if __name__ == "__main__":
    tebak_angka()
