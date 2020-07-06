#For Generate QR
import pyqrcode

qr = pyqrcode.create('hello')
qr.png('abc.png', scale=8)


#For Read QR
from pyzbar.pyzbar import decode
from PIL import Image

d = decode(Image.open('test.png'))

print(d[0].data.decode('ascii'))