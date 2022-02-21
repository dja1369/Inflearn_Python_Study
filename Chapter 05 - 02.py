# Chapter 05 - 02
# 일급 함수(일급 객체)
# 클로저 기초 

#  파이썬의 변수 범위(Scope)

# Ex1

from types import coroutine


def func_v1(a):
    print(a)
    print(b)

# func_v1(10,20) 오류 발생 

# Ex2 

b = 20 

def func_v2(a):
    print(a)
    print(b)

func_v2(10)

# Ex3 

c = 30

def func_v3(a):
    global c 
    print(a)
    print(c)
    c = 40

print(' >> global ', c)
func_v3(10)
print(' >>> local ', c)

# Closure(클로저) 사용 이유 
# 서버 프로그래밍 -> 동시성(Concurrency) 제어 -> 메모리 공간에 여러 자원이 접근 -> 교착상태(Dead Rock)
# 클로저는 함수가 종료되어도 변수의 값을 기억하고 있다.
# Python에선 메모리를 공유하지 않고 메세지 전달로 처리하기 위한 -> Erlang : 병렬 처리 언어.
# 클로저는 공유하되 변경되지 않는다(Immutable, Read Only) 적극적으로 사용 -> 함수형 프로그래밍.
# 클로저는 불변자료구조 및 atom, STM -> 멀티스레드(coroutine) 프로그래밍에 강점

a = 100

print(a + 100)
print(a + 1000)

# 결과 누적(함수 사용)
print(sum(range(1,51)))
print(sum(range(51,101)))



# 클래스 이용 
class Average():
    def __init__(self) -> None:
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        print(f' inner >. {self._series} / {len(self._series)}')
        return sum(self._series) / len(self._series)

# 인스턴스 생성
average_cls = Average()

print(average_cls(10))
print(average_cls(30))
print(average_cls(50))


