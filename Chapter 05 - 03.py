# Chapter 05 - 02
# 일급 함수(일급 객체)
# 클로저 기초 
# 외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근(액세스) 가능

# Closure 사용
from audioop import avg


def closure_ex1():
    # Free Variable
    # Closure 영억 
    series = []
    def average(v):
        series.append(v)
        print(f'inner >> {series} / {len(series)}')
        return sum(series) / len(series)
    return average


avg_closure1 = closure_ex1()

print()
print()

print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))

print()
print()

# Function inspection # inspection : 점검.
print(dir(avg_closure1))
print()
print(dir(avg_closure1.__code__))
print() 
print(avg_closure1.__code__.co_freevars) # series를 여기에 갖고 있음.
print()
print(avg_closure1.__closure__[0].cell_contents) # series의 값들은 여기에 있음.

# 잘못된 클로저 사용


