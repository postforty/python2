# pip install qrcode Pillow
import qrcode

# qr_data = 'www.koreaitjob.co.kr'
# qr_img = qrcode.make(qr_data)
# qr_img.save("koreaitjob.png")

# file_path = r'qr_sample.txt'
# with open(file_path, 'rt', encoding='UTF8') as f:
#     read_lines = f.readlines()

#     for line in read_lines:
#         line = line.strip()
#         print(line)

#         qr_data = line
#         qr_img = qrcode.make(qr_data)

#         qr_img.save(qr_data + '.png')

qr_data = "https://django-app.run.goorm.site/pybo/chart/"
qr_img = qrcode.make(qr_data)
qr_img.save("django-app.png")
