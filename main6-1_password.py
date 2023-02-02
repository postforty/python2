import itertools

passwd_str = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(1, 4):
    to_attempt = itertools.product(passwd_str, repeat = i)
    for attempt in to_attempt:
        passwd = ''.join(attempt)
        print(passwd)
