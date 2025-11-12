import random


def kocok_dadu():
    angka_dadu = random.randint(1, 6)
    return angka_dadu


if __name__ == "__main__":
    print("\n===== selamat datang di mesin dadu otomatis =====")
    while True:
        pilihan = input("mau ngaduk dadu? (y/n): ")
        if "y" in pilihan.lower():
            print("aduk, aduk, aduk...")
            angka = kocok_dadu()
            print("kau dapat angka:", angka, "\n")
        elif "n" in pilihan.lower():
            print("keluar...")
            break
        else:
            print("cuma boelh milih y atau n aja loh!\n")
    print("terima kasih sudah memakai mesin dadu otomatis, sampai jumpa lagi!")
