import itertools
import zipfile

passwd_str = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

zFile = zipfile.ZipFile('secret.zip')

for i in range(4, 5):
    to_attempt = itertools.product(passwd_str, repeat = i)
    for attempt in to_attempt:
        passwd = ''.join(attempt)
        print(passwd)
        try:
            zFile.extractall(pwd = passwd.encode())
            print(f"비밀번호는 {passwd}입니다.")
            break
        except:
            pass
