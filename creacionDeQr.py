import qrcode

# Datos para el QR
data = "https://github.com/Makomakon?tab=repositories"

# Crear un objeto QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Agregar datos al QR
qr.add_data(data)
qr.make(fit=True)

# Crear una imagen del QR
img = qr.make_image(fill='black', back_color='white')

# Guardar la imagen
img.save("qr_code.png")