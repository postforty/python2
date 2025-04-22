import time

s = """첫 줄 타이핑 중입니다.
둘째 줄 타이핑 중입니다.
셋째 줄 타이핑 중입니다."""

def print_typing(s):
    for c in s:
        print(c, end='', flush=True)
        time.sleep(0.2)

print_typing(s)