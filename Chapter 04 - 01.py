# Chapter 04 - 01
# Sequence형 
# Container : 서로다른 자료형[list, tuple, collections.deque]을 담은 자료형
# a = [3, 3.0, 'a]
# Flat : 한개의 자료형[str, bytes, bytearrays, array.array, memoryview]
# mutable 가변(list, bytearray, array, memoryview, deque)
# immutable 불변(tuple, str, bytes)
# 리스트및 튜플 고급

# 지능형 리스트 (list comprehension)

chars = '+_)(%&^#$#@)'

code_list1 = []

for s in chars:
    # ord : 입력받은 값 유니코드로 반환 
    # chr : 입력받은 값를 값으로 반환 
    # unicode_list
    code_list1.append(ord(s))

print(code_list1)

# Comprehending Lists
code_list2 = [ord(s) for s in chars]

print(code_list2)

# Comprehending Lists + Map, Filter
# 40번 이상인 유니코드 반환
code_list3 = [ord(s)for s in chars if ord(s) >= 40]
code_list4 = list(filter(lambda x : x >= 40, map(ord, chars)))

print(code_list1)
print(code_list1)
print(code_list3)
print(code_list4)
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

print()
print()

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지X 효율성O)
# 생성, 메모리의 효율성
# sequence 결과값을 만들어내고 로컬상태를 유지하며 다음번 반환할 값을 정확하게 가지고 있다.
# array는 Flat 형태 이므로 가변형이고 한개의 자료형만 넣을수있다.

import array
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))


print(type(tuple_g))
print(tuple_g)
# 다음값 반환.
print(next(tuple_g))
print(array_g)
print(type(array_g))
print(array_g.tolist())
print(type(array_g))

print()
print()
# 제네레이터 예제

print(('%s' % c + str(n) for c in ['A','B','C','D'] for n in range(1,21)))

for s in ('%s' % c + str(n) for c in ['A','B','C','D'] for n in range(1,21)):
    print(s,end=" , ")


print()
print()

# 리스트 주의, 깊은 복사 : 데이터 자체를 통채로 복사함, 복사된 두 객체는 완전히 독립적인 메모리 차지, value type의 객체들은 깊은복사를 함.
marks1 = [['~'] * 3 for n in range(4)]
# 이렇게 해도 작동은 하나 수정시에 문제 발생, 얕은 복사 : 최소한의 복사를함, 값을 복사하는게 아니라 주소값을 복사하여 출력하게 됨으로 내용변경시 주소값 자체가 바뀌어 모두 변경됨
marks2 = [['~'] * 3] * 4
print(marks1)
print(marks2)


marks1[0][1] = 'X'
marks2[0][1] = 'X'

print(marks1)
print(marks2)

# 증명
print([id(i) for i in marks1])
print([id(i) for i in marks2])