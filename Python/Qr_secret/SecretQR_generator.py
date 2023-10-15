import qrcode


data ="Type your message here"

qr = qrcode.QRCode(
    version=1,  # QR code version (adjust as needed)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # Size of each QR code box
    border=4,     # Size of the border around the QR code
)

qr.add_data(data)
qr.make(fit=True)
qr_image = qr.make_image(fill_color="black", back_color="white")

qr_image.save("my_qr_code.png")
qr_image.show()