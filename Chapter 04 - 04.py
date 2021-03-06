# Chapter 04 - 04
# Sequence형 
# HashTable -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 X, set -> 중복 허용 X
# Dict 및 Set 심화 

# Immutable Dict 생성법
# 필수로 선언해야하는 라이브러리 
from types import MappingProxyType

d = {'key1' : 'value1'}

# Read Only 수정할수 없게 선언함. Frozen
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))

# 수정 불가 
# d_frozen['key2'] = 'value2'

# 수정 가능
d['key2'] = 'value2'

print()
print()
print()

s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set() # Not {}
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

s1.add('Melon')
print(s1)

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))


# 선언 최적화
# 바이트 코드 실행 > 파이썬 인터프리터 실행.
from dis import dis

print('-------')
print(dis('{10}'))
print('-------')
print(dis('set([10])'))

# 지능형 집합(Comprehending Set)

print('------')

from unicodedata import name

print({name(chr(i), '') for i in range (0,256)})
