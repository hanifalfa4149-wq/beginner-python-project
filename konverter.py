import requests

# install dulu modules nya kalo belum ada
# pip install requests


def Konversi_celsius_ke_fahrenheit(suhu_celsius):
    return (suhu_celsius * 9 / 5) + 32


def konversi_fahrenheit_ke_celsius(suhu_fahrenheit):
    return (suhu_fahrenheit - 32) * 5 / 9


def konverter_mata_uang_api(jumlah, dari_mata_uang, ke_mata_uang):
    try:
        response = requests.get(
            f"https://open.er-api.com/v6/latest/{dari_mata_uang.upper()}"
        )
        data = response.json()

        if response.status_code == 200 and data["result"] == "success":
            rates = data["rates"]
            if dari_mata_uang.upper() not in rates or ke_mata_uang.upper() not in rates:
                return "kode mata uang tidak valid(s)."

            jumlah_dikonversikan = jumlah * rates[ke_mata_uang.upper()]
            return f"{jumlah_dikonversikan:.2f}"
        else:
            return f"Kesalahan dalam memuat nilai: {data.get('tipe error', 'error tidak diketahui')}"

    except requests.exceptions.ConnectionError:
        return "Kesalahan jaringan, coba cek lagi koneksi internet mu."
    except Exception as e:
        return f"Terjadi kesalahan tidak terduga: {e}"


def convert_cm_to_feet_inches(value_cm):
    inches = value_cm / 2.54
    feet = int(inches // 12)
    remaining_inches = inches % 12
    return f"{feet} feet and {remaining_inches:.2f} inches"


def convert_feet_inches_to_cm(feet, inches):
    total_inches = (feet * 12) + inches
    length_cm = total_inches * 2.54
    return f"{length_cm:.2f}"


if __name__ == "__main__":

    def konverter_suhu_cli():
        print("\nkamu mau mengonversikan suhu apa? pilih salah satu")
        print("1. Celsius ke Fahrenheit")
        print("2. Fahrenheit ke Celsius")
        try:
            choice = int(input("masukkan pilihanmu (1 / 2) : "))
            if choice == 1:
                suhu = float(input("masukkan suhu dalam celcius : "))
                print(
                    f"{suhu} derajat celcius sama dengan {Konversi_celsius_ke_fahrenheit(suhu):.2f} derajat fahrenheit.\n"
                )
            elif choice == 2:
                suhu = float(input("masukkan suhu dalam fahrenheit : "))
                print(
                    f"{suhu} derajat fahrenheit sama dengan {konversi_fahrenheit_ke_celsius(suhu):.2f} derajat celsius.\n"
                )
            else:
                print("Cuma boleh milih 1 atau 2 brooo\n")
        except ValueError:
            print("Tolong masukkan angka aja.\n")

    def konverter_mata_uang_cli():
        print("\n--- KONVERTER MATA UANG REAL-TIME ---")
        try:
            dari_mata_uang = input(
                "Pilih mata uang (Contohnya USD, GBP, UER, IDR): "
            ).upper()
            jumlah = float(input("masukkan jumlah: "))
            ke_mata_uang = input("ke mata uang (Contohya USD, GBP, EUR, IDR): ").upper()
            result = konverter_mata_uang_api(jumlah, dari_mata_uang, ke_mata_uang)
            print(f"{jumlah} {dari_mata_uang} setara dengan {result} {ke_mata_uang}\n")
        except ValueError:
            print("Jumlah tidak valid, tolong masukkan angka aja.\n")

    def konverter_panjang_cli():
        print("\nApa yang ingin kamu konversikan?")
        print("1. Sentimeter ke kaki dan inci")
        print("2. kaki dan inci ke sentimeter")
        try:
            choice = int(input("Maukkan pilihanmu (1 / 2): "))
            if choice == 1:
                value = float(input("Masukkan panjang dalam cm: "))
                print(
                    f"{value} Sentimeter sama dengan {convert_cm_to_feet_inches(value)}\n"
                )
            elif choice == 2:
                feet = float(input("Masukkan panjang dalam satuan kaki: "))
                inches = float(input("Masukkan panjang dalam satuan inci: "))
                print(
                    f"{feet} Kaki dan {inches} inci dalam sentimeter jadinya {convert_feet_inches_to_cm(feet, inches)}\n"
                )
            else:
                print("IInput salah. Coba lagi\n")
        except ValueError:
            print("Input salah. Masukkan angka aja brooo.\n")

    print("===== SELAMAT DATANG DI KONVERTER =====")
    while True:
        print("kamu mau pilih yang mana? pilih salah satu")
        print("1. Mengkonversikan suhu")
        print("2. Mengkonversikan mata uang")
        print("3. Mengkonversikan panjang")
        print("4. keluar")
        try:
            choice = int(input("masukkan pilihanmu (1 - 4) : "))
            if choice == 1:
                konverter_suhu_cli()
            elif choice == 2:
                konverter_mata_uang_cli()
            elif choice == 3:
                konverter_panjang_cli()
            elif choice == 4:
                print(
                    "Terima kasih sudah menggunakan konverter ini. Sampai jumpa lagi!"
                )
                break
            else:
                print("cuma boleh milih 1 - 4.\n")
        except ValueError:
            print("yang dimasukkan itu angka.\n")
