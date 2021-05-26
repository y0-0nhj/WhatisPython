# 2021/01/05

'''
집합(set) 자료형
- 집합에 관련된 데이터를 쉽게 처리하는 데이터 타입
- 중복된 값을 허용 불가
- 순서가 유지 되지 않음, 인덱싱 사용 불가
'''

a = {'korea', 'swiss', 'france', 'italia'}
print(a)
print(type(a))
print(len(a))

# 빈 셋
b = set()
print(b)
print(type(b))

# 셋의 추가/삭제
a.add('england')
print(a)
print(len(a))

a.add('swiss') # 중복 데이터 추가되지 않음
print(a)
print(len(a))

a.remove('france')
print(a)
print(type(a))

# 셋 병합
b = {'korea', 'china', 'japan', 'vetnam'}
a.update(b) # a에 b를 병합
print(a)
print(type(a))
print(len(a))

# 셋을 리스트, 튜플로 변환
x = list(a)
print(x)
print(type(x))

y = tuple(a)
print(y)
print(type(y))
print()
print("----------")

# < 집합 관련 함수 >
# 교집합(&), 합집합(|), 차집합(-), 배타적 차집합(^)

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

# s1 = set([1, 2, 3, 4])
# s2 = set([3, 4, 5, 6])

# 교집합 - 두 개의 집합에 공통적으로 존재하는 값
# s3 = s1 & s2
s3 = s1.intersection(s2)
print(s3)

# 합집합 - 두 개의 집합을 값을 합침, 공통적인 요소는 한번만 표현.
# s4 = s1 | s2
s4 = s1.union(s2)
print(s4)

# 차집합 - 왼쪽 집합에서 오른쪽 집합의 요소를 삭제
# s5 = s1 - s2
s5 = s1.difference(s2)
print(s5)

# 배타적 차집합 - 두 개의 집합에서 한쪽에만 있는 요소를 표현
# s6 = s1 ^ s2
s6 = s1.symmetric_difference(s2)
print(s6)
