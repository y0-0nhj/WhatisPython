# 2021/01/13(수)

'''
기타 내장 함수
'''
# input(), print(), type(), len(), id(), help()
# iter(), next(), enumerate(), range()

# 1.  타입 변환 함수
# int() : 정수로 변환하는 함수
# float() : 실수로 변환하는 함수
# str() : 문자열로 변환하는 함수
# bool() : 논리형으로 변환하는 함수

'''
a = '10'
print(type(a))
a = int(a)
print(type(a))

a = '3.14'
print(type(a))
a = float(a)
print(type(a))

a = 10
print(type(a))
a = str(10)
print(type(a))

a = 'True'
print(type(a))
a = bool(a)
print(type(a))
print('----------')
'''

# 2. 리스트, 튜플, 딕션너리, 셋을 만드는 함수
# list(), tuple(), dict(), set() : 빈 컬렉션을 생성
'''
a = list()
print(type(a))
print(a)

a = tuple()
print(type(a))
print(a)

a = dict()
print(type(a))
print(a)

a = set()
print(type(a))
print(a)
print('----------')
'''

# 3. 진법 변환 함수
# bin() : 2진수로 변환하는 함수
# hex() : 16진수로 변환하는 함수
# oct() : 8진수로 변환하는 함수
'''
a = 31
print(a)
print(bin(a)) # 0b11111
print(hex(a)) # 0x1f
print(oct(a)) # 0o37
print('----------')
'''

# 4. 아스키 코드 관련 함수
# chr() : 숫자에 해당하는 문자를 알려주는 함수
# ord() : 문자에 해당하는 숫자를 알려주는 함수
# A ~ Z : 65 ~ 90
# a ~ z : 97 ~ 122
'''
print(chr(65+25)) 
print(chr(97+25))

print(ord('X'))
print(ord('x'))
print('----------')
'''

# 5. 수학과 관련된 함수
# round() : 반올림 함수
# abs() : 절대값을 구하는 함수
# pow() : 승수를 구하는 함수
# sum() : 리스트나 튜플의 합계를 구하는 함수
# max() : 리스트나 튜플에서 최댓값을 구하는 함수
# min() : 리스트나 튜플에서 최소값을 구하는 함수
# divmod() : 나눗셈의 몫과 나머지를 튜플로 만들어 주는 함수
# sorted() : 리스트나 튜플을 정렬하는 함수
'''
a = 34567.56789
print(round(a))
print(round(a, 1))
print(round(a, 2))
print(round(a, 0))
print(round(a, -1))
print(round(a, -2))

print(abs(-11))
print(pow(2, 3))
print(pow(3, 4))

print(sum([10, 20, 30, 40, 50]))
print(min([10, 20, 30, 40, 50]))
print(max([10, 20, 30, 40, 50]))

print(10 / 3)
print(10 // 3)
print(10 % 3)
print(divmod(10, 3))

print(sorted([92, 65, 85, 77, 96, 68, 88]))
print(sorted([92, 65, 85, 77, 96, 68, 88], reverse=True))
'''
# 5. 참, 거짓을 판별하는 함수
# 반복가능한 데이터 : 리스트, 튜플, 문자열, 딕셔너리, 집합
# all() : 반복가능한 데이터에서 모든 요소가 참일 때 전체 결과가 참인 함수
# any() : 반복가능한 데이터에서 전체 요소 중 하나라도 참이 있을 때 전체 결과가 참인 함수 
'''
print(all([1, 2, 3, 0]))
print(any([1, 2, 3, 0]))

s = ['a', 'b', 'c', '']
print(all(s))
print(any(s))
print('----------')
'''
# 6. 함수의 설명과 목록을 보여주는 함수
# help() : 함수의 설명, 사용법
# dir() : 객체에서 사용할 수 있는 함수들의 목록 확인
'''
a = []
print(dir(a))
print('----------')

b = ()
print(dir(b))
'''

##### 기타 함수 #####
# 7. enumerate() : 리스트나 튜플에서 인덱스를 사용할 수 있도록 하는 함수

names = ['이익준', '김준완', '채송화', '양석형', '안정원']

# 7-1. 값만 출력
for n in names:
    print(n)
print('----------')

# 7-2. 인덱스와 값 출력
i = 0
for n in names:
    print(i, n)
    i += 1
print('----------')

# 7-3. 인덱스와 값 출력
for i, name in enumerate(names):
    print(i, name)
print('----------')

# 7-4. 인덱스와 값을 튜플로 만들어 출력
for item in enumerate(names):
    # print(type(item))
    print(item)
print('----------')

# 8. filter() : 함수와 반복가능한 데이터(리스트)를 받아서 처리하는 함수
# 예제) 데이터를 받아서 양수만 리스트로 저장하는 함수를 생성하시오.
'''
# 1번 방법
def choose(data):
    result = []
    for i in data:
        if i > 0:
            result.append(i)
    return result

s = [10, -10, -5, 0, 35, 77, -33, 87, 99, -55]
a = choose(s)
print(a)
'''

# 2번 방법
def choose(data):
    return data > 0;

s = [10, -10, -5, 0, 35, 77, -33, 87, 99, -55]
a = list(filter(choose, s))
print(a)























