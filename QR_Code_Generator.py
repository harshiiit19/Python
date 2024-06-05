import pyqrcode
from pyqrcode import QRCode

# string whichi reprsented th Qr code 
s = "https://www.google.com/"

# generated Qr code
url = pyqrcode.create(s)

#created and save thr png file naming "myqr.png"
url.svg("mygoogle.svg" , scale= 25)