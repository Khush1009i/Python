import qrcode
import image

qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5  # it's the white part of image -- border in all 4side with white color
)

#data = "https://www.youtube.com/watch?v=onHPipeASdk&list=PLpp8-k7G_6Y3Wj1suZQ-9lATFzFuGw93x&index=1"
# as I've given path of a channel like the same u can give anything.
# if u dont wont to redirect

data = "https://6738dcf05a707db08bf0e106--delightful-marshmallow-064997.netlify.app/"
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fit = "black", back_color="white")
img.save("QR-code.png")