# 이터러블 객체 만들기

# 클래스 패턴
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration.')
        self._idx += 1
        return word

    def __repr__(self):  # 출력될 수 있는 표현(printable representation)
        return f'WordSplit({self._text})'


greeting = WordSplitter("Hello Python!")
print(greeting)  # WordSplit(['Hello', 'Python!'])
print(next(greeting))  # Hello
print(next(greeting))  # Python!
# print(next(greeting))  # StopIteration

print()

# 제너레이터(generator) 패턴
# - 발생자, 이터레이터를 생성해주는 함수
# - 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가하면 메모리 사용량 증가하기 때문에 제너레이터 권장
# - 작은 메모리 조각 사용
# - 단위 실행 가능한 코루틴(Coroutine) 구현과 연동


class WordSplitterGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word
        return

    def __repr__(self):  # 출력될 수 있는 표현(printable representation)
        return f'WordSplitGenerator({self._text})'


greeting = WordSplitterGenerator("Hello Python!")
print(greeting)
greeting_iter = iter(greeting)
print(next(greeting_iter))
print(next(greeting_iter))
# print(next(greeting_iter)) # StopIteration
