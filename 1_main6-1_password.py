import itertools
import zipfile

passwd_str = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def un_zip(passwd_str, min, max, zFile):
    zFile = zipfile.ZipFile(zFile)
    for i in range(min, max+1):
        to_attempt = itertools.product(passwd_str, repeat = i)
        for attempt in to_attempt:
            passwd = ''.join(attempt)
            # print(passwd)
            try:
                zFile.extractall(pwd = passwd.encode())
                print(f"비밀번호는 {passwd}입니다.")
                return 1
            except:
                pass

result = un_zip(passwd_str, 4, 4, 'secret.zip')

if result == 1:
    print("암호찾기 성공!")
else:
    print("암호찾기 실패!")


