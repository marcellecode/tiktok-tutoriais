import qrcode
qr = qrcode.QRCode(
    version=1,
    box_size=15,
    border=2,
)
qr.add_data('<Coloque aqui o link ou a informação que terá no QRCode>')
qr.make(fit=True)

img = qr.make_image(back_color="black", fill_color=(255, 195, 235))
type(img) 
img.save("NOME DO ARQUIVO.png")