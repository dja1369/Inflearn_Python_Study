# Chapter 04 - 03
# Sequence형 
# Container : 서로다른 자료형[list, tuple, collections.deque]을 담은 자료형
# a = [3, 3.0, 'a]
# Flat : 한개의 자료형[str, bytes, bytearrays, array.array, memoryview]
# mutable 가변(list, bytearray, array, memoryview, deque)
# immutable 불변(tuple, str, bytes)
# 해시테이블 
# Key에 Value를 저장하는 구조 ? Dict => 파이썬 Dict는 해쉬 테이블의 대표적인 예
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조
# Key 값을 해싱 함수를 통해 -> 해시 주소가 나오고 -> 이를통해 Key에 대한 value 참조.

# Dict 구조 
# print(__builtins__.__dict__)

# 튜플 in 튜플
t1 = (10, 20, (30, 40, 50))
# 튜플 in 리스트
t2 = (10, 20, [30, 40, 50])

# 불변형인 튜플은 정상적으로 작동함
print(hash(t1))

# 가변형인 list는 예외가 발생한다.
# print(hash(t2))
print()
print()

# Dict Setdefault 예제 
source = (('k1', 'val1'),
         ('k1', 'val2'),
         ('k2', 'val3'),
         ('k2', 'val4'),
         ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No Use Setdefault
for k,v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]
print(new_dict1)


# use Setdefault
for k,v in source:
    new_dict2.setdefault(k,[]).append(v)
print(new_dict2)


print()
print()  
print()