# 2021/01/25(월)

'''
< 파이썬에 사용하는 데이터 타입 >
- 값을 대입할 때 정해짐.
1. 숫자형
- 정수형 : int
- 실수형 : float

# 연속적인 데이터의 값 - 문자열, 리스트(list), 튜플(tuple), 딕셔너리(dictionary), 셋(set) 
2. 문자열 : str
- '', "", 둘 중의 하나로 감싸면 됨.
- 인덱스가 있음 (indexing, slicing)

3. 리스트(list) : 여러 개의 값을 하나의 데이터로 다루는 방법, 가변
- 자유롭게 값을 추가하고, 수정하고, 삭제할 수 있는 타입
- [], list() 함수
- 인덱스가 있음 (indexing, slicing)

4. 튜플(tuple) : 여러 개의 값을 하나의 데이터로 다루는 방법, 불변
- 추가, 수정, 삭제를 할 수 없는 타입
- (), tuple() 함수
- 인덱스가 있음 (indexing, slicing)

5. 딕셔너리(dictionary) : 여러 개의 값을 하나의 데이터로 다루는 방법
- 하나의 값이 반드시 key와 value로 구성됨.
- 인덱스가 없음.
- key를 통해 value를 구함.
- {key:value}, dict(key:value)

6. 셋(set) : 여러 개의 값을 하나의 데이터로 다루는 바업
- 인덱스는 없음.
- {}, 값만 존재

a = 10
b = 10.5
s = 'hello'

print(type(a))
print(type(b))
print(type(s))

# 리스트(list)
a = []
a = list()
b = [10]
c = [10, 20, 30, 40, 50]
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

# 튜플(tuple)
a = ()
a = tuple()
b = (10,)
c = (10, 20, 30, 40, 50)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

d = list(c)
print(d)
print(type(d))

# 딕셔너리(dictionary)
a = {}
a = dict()
b = {'name':'이익준', 'tel':'010-1111-1111', 'score':95}
print(a)
print(b)
print(type(a))
print(type(b))

# 셋(set)
# a = {} # 딕셔너리
a = set()
b = {10}
c = {10, 20, 30}
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
'''

# 1. 리스트를 다루는 방법
# - 인덱스(index) : 왼쪽에서 0으로 시작하여 1씩 증가하는 번호
# - 인덱싱(indexing) : 인덱스를 통해서 하나의 값을 얻는 방법
# - 슬라이싱(slicing) : 인덱스를 통해서 범위의 값을 추출하는 방법
'''
a = [10, 20, 30, 40, 50]
print(a[0])
print(a[4])
print(a[1:3])
print(a)
print(a[0:5])
print(a[:])
print(a[1:])
print(a[:4])

# 2중 리스트
a = [10, 20, ['a', 'b', 'c', 'd', 'e'], 30, 40, 50]
print(a)
print(type(a))
print(a[2])
print(a[2][2])
print(a[2][1:4])
print(a[-4])
print(a[-4][3:])

del(a[4])
print(a)

a[1] = 60
print(a)

del(a[2][2])
print(a)

a[2][0] = 'x'
print(a)

# 인덱스를 통해서 삭제와 변경은 가능
# 추가는 함수를 통해서 가능
#a[5] = 70
print(a)
'''

'''
a = [10, 20, 30, 40, 50]
print(a)

a.append(60) # 맨 뒤에 값을 추가
print(a)

a.insert(2, 70) # 중간에 값을 추가
print(a)

a.remove(70) # 값을 삭제
print(a)
    
# a.clear() # 모든 값을 삭제
a.reverse()
print('a = ', a)

b = a.copy()
print('b = ', b)

a = [55, 15, 75, 35, 25, 45, 65]
# a.sort() # 오름차순
a.sort(reverse=True) # 내림차순
print(a)
print(len(a))
print(a.pop(0))
print(a)

a = [10, 20, 30, 10, 20, 30, 10]
b = [40, 50, 60]
print(a.count(10)) # 값이 나온 횟수를 출력

#a.extend(b)
#a = a + b # 연결
a += b
print(a)
'''

'''
a = [10, 20, 30, 40, 50]

# 1. 추가
a.append(60) # 맨 뒤로 추가
a.insert(1, 70) # 중간에 추가, 1번 인덱스에 70 추가

# 2. 변경 - 인덱스를 통해 값을 변경
a[2] = 80

# 3. 삭제
del a[3] # del(a[3]), 인덱스를 통해 삭제
a.remove(10) # 10이라는 값을 삭제
a.pop() # 맨 뒤의 값을 리턴하고 삭제
a.pop(3) # 3번 인덱스의 값을 리턴하고 삭제
a.clear() # 모든 값을 삭제

help(list)
help(tuple)
'''

'''
# 튜플
a = (10, 20, 30, 40, 50)
print(a)
print(a[0]) # 인덱싱 가능
print(a[1:4]) # 슬라이싱 가능
print(a.index(10))
print(a.count(50))

# a[2] = 60    # 튜플은 수정 불가
# del(a[2])    # 튜플은 삭제 불가
# a.append(50) # 튜플은 추가 불가
'''

# 딕셔너리(dictionary)
# - key와 value의 쌍을 저장하는 타입
# - 순차적인 구조이지만, 순서는 없음
# - 키를 통해 값을 구하는 구조
# - 키는 중복 불가, 값은 중복 가능
# - 키로는 리스트는 사용불가, 튜플은 사용가능

d = {'name':'이익준', 'age':42, 'tel':'010-1111-1111'}
print(d)

# 1. 추가 : 키와 값의 쌍으로 데이터를 추가
d['job'] = '간담췌 외과'
print(d)

# 2. 수정 : 키의 중복을 허용하지 않으므로, 저장한 최종값으로 수정됨.
d['age'] = 38
print(d)

# 3. 삭제 : 키를 통해서 데이터 삭제
del d['tel']
print(d)

# 4. 출력 : 키를 통해 값을 출력
print(d['name'])
print(d.get('name'))

# 딕셔너리의 다양한 함수
print(d.keys())   # 딕셔너리의 모든 키 확인
print(d.values()) # 딕셔너리의 모든 값 확인
print(d.items())  # 딕셔너리 키와 값을 모두 확인
print('----------')

# 딕셔너리의 모든 키에 대한 값을 출력하는 방법
for k in d.keys():
    #print('{}({})'.format(k, d.get(k)))
    print('{}({})'.format(k, d[k]))
