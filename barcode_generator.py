import qrcode
import os

def generate_qr(data, filename="my_qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"✅ QR Code saved as: {filename}")

    os.startfile(filename)

# Example usage
data = "https://github.com/markdennis2121"
generate_qr(data)
