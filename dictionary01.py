# 2021/01/05(화)

'''
딕셔너리(dictionary) 자료형
- 키(key)와 값(value)의 쌍을 저장하는 데이터 구조, 자바의 맵 구조
- 리스트나 튜플은 순차적인 구조이나, 딕셔너리 순서가 없음.
- 키를 통해서 값을 구하는 구조
- 키는 중복 불가, 값은 중복 가능
- 키는 변경 불가, 키로 튜플은 사용가능하지만, 리스트는 사용 불가
'''

a = {'name':'tom', 'phone':'010-1111-1111', 'birthday':'19961020'}
print(a)
print(type(a)) # <class 'dict'>

# 딕션너리 요소 추가 - a[key] = value
a = {1:'a'}
print(a)
a[2] = 'b' # 키와 값
print(a)
a['name'] = 'tom'
print(a)
a[3] = ['a', 'b', 'c']
print(a)

# 딕셔너리 요소 삭제 - 키를 통해 값을 삭제
del(a[2])
print(a)

# 딕셔너리의 키를 통해 값을 출력
print(a[1])
print(a['name'])
# print(a[2]) # KeyError: 2
print(a[3])

# 딕셔너리의 키를 값을 수정
a[1] = 'hi'
print(a)

# 딕셔너리의 키 : 변하지 않는 값을 사용
# - 딕셔너리의 키로 리스트는 사용 불가, 튜플은 사용 가능
# 딕셔너리의 값 : 변하는 값과 변하지 않는 값을 모두 사용

a[3.14] = 'PI'
print(a)

# b = {1:'a', 3.14:'PI', 'name':'tom', [1,3,5]:'odd'} # 리스트는 키로 사용 불가
b = {1:'a', 3.14:'PI', 'name':'tom', (1,3,5):'odd', 'list':[1,2,3], 'tuple':(4,5,6)}
print(b)

# < 딕셔너리의 다양한 함수 > 
a = {'name':'tom', 'phone':'010-1111-1111', 'birth':'1996/10/20'}
print(a)

# 딕셔너리의 키 확인
print(a.keys()) # dict_keys(['name', 'phone', 'birth'])

for k in a.keys():
    print(k)

# 딕셔너리의 키를 리스트 변환 - list() 함수 사용
k = list(a.keys())
print(k)
print(type(k))

# 딕셔너리의 값 확인
print(a.values())
v = list(a.values())
print(v)
print(type(v))

# 딕셔너리의 키와 값을 한꺼번에 확인
print(a.items())

# 딕셔너리의 모든 요소를 삭제
# a.clear()
print(a)
print()
print("----------")

# < 키를 통해서 값을 얻는 방법 1 >
print(a['name'])
# print(a['age']) # error 발생 - 키가 존재하지 않음

# < 키를 통해서 값을 얻는 방법 2 >
print(a.get('name'))
print(a.get('name', 'name 키는 없습니다.'))
print(a.get('age')) # None, 에러가 발생하지 않음, 그 다음 내용의 처리가 이루어짐.
print(a.get('age', 'age 키는 없습니다.')) # 키가 없을 때 디폴트 값 설정
print(a)

# 딕셔너리의 키의 존재 유무 확인 - in 연산자
print('name' in a) # True
print('age' in a)  # False

if 'name' in a:
    print('이름은', a.get('name'), '입니다.')
else:
    print('이름은 사전에 존재하지 않습니다.')


if 'age' in a:
    print('나이는', a.get('age'), '입니다.')
else:
    print('나이는 사전에 존재하지 않습니다.')

a = {'id':'aaa1111', 'name':'이익준'}
b = {'age':40}
print(a)
print(b)
print(type(a))
print(type(b))

# 두 개의 딕셔너리를 병합하는 방법
a.update(b) # a에 b를 병합하는 방법
print(a)

# 빈 딕셔너리 생성
#a = []
#b = ()
#c = {}
a = list()
b = tuple()
c = dict()

print(a)
print(b)
print(c)

