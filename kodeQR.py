import pyqrcode
from PIL import Image

# installasi library yang dibutuhkan:
# pip install pyqrcode
# pip install pillow

link = input("masukkan link yang ingin diubah menjadi kode QR: ")
kodeQR = pyqrcode.create(link)
kodeQR.png("kodeQR.png", scale=6)
Image.open("kodeQR.png")
