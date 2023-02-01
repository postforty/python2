import qrcode

qr_data = 'http://www.koreaitjob.co.kr/'
qr_img = qrcode.make(qr_data)

qr_img.save('koreaitjob.png')