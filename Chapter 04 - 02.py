# Chapter 04 - 02
# Sequence형 
# Container : 서로다른 자료형[list, tuple, collections.deque]을 담은 자료형
# a = [3, 3.0, 'a]
# Flat : 한개의 자료형[str, bytes, bytearrays, array.array, memoryview]
# mutable 가변(list, bytearray, array, memoryview, deque)
# immutable 불변(tuple, str, bytes)
# 리스트및 튜플 고급

# Tuple Advance
# Unpacking

# b, a = a, b

# divmod(값,나눌값) : 몫과 나머지를 반환해준다.
print(divmod(100,9))
print(divmod(*(100,9)))
# Tuple을 해제한다.
print(*(divmod(100,9)))


print()

# *을 붙이면 알아서 Packing을 해줌.
x, y, *rest = range(10)
print(x,y,rest)

x, y, *rest = range(2)
print(x,y,rest)

x, y, i, *rest = 1,2,3,4,5
print(x, y, i, rest)

print()
print()

# Mutable(가변), Immutable(불변)

l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
print(m, id(l))

l = l * 2
m = m * 2

print(l, id(l))
print(m, id(l))

l *= 2
m *= 2

print(l, id(l))
print(m, id(l))

print()
print()

# 정렬할때 사용.
# sort vs sorted
# reverse : 반대로 정렬, key : 길이 옵션, key : str.lower(문자열의 소문자순으로 정렬)

# sorted : 정렬후 새로운 객체로 반환 (원본 변화 X)
f_lists = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
# 그냥 정렬.
print('sorted = ', sorted(f_lists))
# 역순으로 정렬.
print('sorted = ', sorted(f_lists, reverse=True))
# 길이순으로 정렬됨.
print('sorted = ', sorted(f_lists, key=len))
# 람다 사용 [-1] 음수는 끝부터 시작한다는 의미이다. 끝의 인덱스를 기준으로 정렬
print('sorted = ', sorted(f_lists, key=lambda x : x[-1])) 
print('sorted = ', sorted(f_lists, key=lambda x : x[-1],reverse=True))


print(f_lists)

# sort : 정렬후 기존 객체 변경 (원본 변화 O)

# 반환 값 확인(None)
print('sort = ', f_lists.sort())
print('sort = ', f_lists.sort(reverse=True), f_lists)
print('sort = ', f_lists.sort(key = len), f_lists)
print('sort = ', f_lists.sort(key=lambda x:x[-1]), f_lists)
print('sort = ', f_lists.sort(key=lambda x:x[-1], reverse = True), f_lists)

# List Vs Arrays 적합한 사용법 설명
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반 : 배열(리스트와 거의 호환됨), 빠른 실행속도