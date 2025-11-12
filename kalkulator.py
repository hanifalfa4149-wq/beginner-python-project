def hitung(angka1, operasi, angka2):
    if operasi == "+":
        return angka1 + angka2
    elif operasi == "-":
        return angka1 - angka2
    elif operasi == "*":
        return angka1 * angka2
    elif operasi == "/":
        if angka2 == 0:
            return "Error: Pembagian dengan nol tidak diperbolehkan."
        return angka1 / angka2


if __name__ == "__main__":
    print("===== selamat datang di kalkulator CLI =====\n")
    while True:
        print("pilih operators: +, -, *, / atau keluar")
        operasi = input("Pilih operator: ")

        if operasi == "keluar":
            break

        if operasi not in "+-*/":
            print("operator salah.")
            continue

        angka1 = float(input("masukkan angka pertama: "))
        angka2 = float(input("masukkan angka kedua: "))

        hasil = hitung(angka1, operasi, angka2)
        print(f"Output: {hasil}")
