import qrcode

import os
if __name__ == "__main__":
    def generate_qr(data, filename="my_qrcode.png"):
        # Configure the QR Code settings
        qr = qrcode.QRCode(
            version=1,  # Controls size (1 is 21x21 modules)
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
            box_size=10,  # Pixel size of each box
            border=4  # Thickness of the border
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Generate the image
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
        print(f"QR Code saved as {filename}")

        # Open the image (Windows only)
        os.startfile(filename)

    # Example usage
    data = "https://github.com/markdennis2121"
    generate_qr(data)
