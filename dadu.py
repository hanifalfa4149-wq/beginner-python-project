import random


def roll_die():
    die_number = random.randint(1, 6)
    return die_number


if __name__ == "__main__":
    print("\n===== selamat datang di mesin dadu otomatis =====")
    while True:
        choice = input("mau ngaduk dadu? (y/n): ")
        if "y" in choice.lower():
            print("aduk, aduk, aduk...")
            number = roll_die()
            print("kau dapat angka:", number, "\n")
        elif "n" in choice.lower():
            print("keluar...")
            break
        else:
            print("dah dibilang cuma boleh y atau n, apa kau tekan tu? ulang lagi.")
