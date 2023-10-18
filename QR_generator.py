import qrcode
import image
qr = qrcode.QRCode(
    box_size=10,
    version=15,
    border=5
)
data = input("Paste info that you want to make QR!\n")
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
name = input("Save file as\n")
img.save(name)


