def calculate(angka1, operasi, angka2):
    if operasi == "+":
        return angka1 + angka2
    elif operasi == "-":
        return angka1 - angka2
    elif operasi == "*":
        return angka1 * angka2
    elif operasi == "/":
        if angka2 == 0:
            return "Error: Division by zero"
        return angka1 / angka2


if __name__ == "__main__":
    print("===== selamat datang di kalkulator CLI =====\n")
    while True:
        print("Operators: +, -, *, / atau keluar")
        operasi = input("masukkan operator: ")

        if operasi == "keluar":
            break

        if operasi not in "+-*/":
            print("operator salah.")
            continue

        angka1 = float(input("masukkan angka pertama: "))
        angka2 = float(input("masukkan angka kedua: "))

        result = calculate(angka1, operasi, angka2)
        print(f"Output: {result}")
