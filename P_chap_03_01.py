# Chap03-01
# Special Method (Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Function), 클래스(Class)
# 클래스안에 정의할 수 있는 특별한(Bulit-In) 메소드

# 기본형
print(int)
print(float)

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

n = 10

print(type(n))

# 내부적으로 클래스가 호출되어 사용되며 구현이 되어있다.
print(n + 100)
print(n.__add__(100))
# print(n.__doc__)
print(n.__bool__(),bool(n))
print(n * 100)
print(n.__mul__(100))

print()
print()

# 클래스 예제1
class Fruit():
    def __init__(self, name, price):
        self._name = name
        self._price = price
    def __str__(self):
        return f'Fruit Class Info {self._name}, {self._price}'

    def __add__(self, x):
       # return (self._price + x._price) 기존의 add가 호출되었을때 매직메소드를 선언하여 내마음대로 재정의할수 있다.
       # 코드의 간결화, 가독성 증가, 기능 개선 가능
        print("called add")
        return self._price + x._price

    def __sub__(self, x):
        print("called sub")
        return self._price - x._price

    def __le__(self, x):
        print("called le")
        if self._price <= x._price:
            return  True
        else:
            return False

    def __ge__(self, x):
        print("called ge")
        if self._price >= x._price:
            return  True
        else:
            return False
# 인스턴스 생성
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banan', 3000)

print(s1 + s2)
print(s2 - s2)

# 일반적인 계산
print(s1._price + s2._price)
print(s1._price - s2._price)

# 매직메소드
print(s1 >= s2)
print(s1 <= s2)
print(s1 + s2)
print(s1 - s2)
print(s1)
print(s2)