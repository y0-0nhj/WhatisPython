# 2021/01/04(월)

"""
컬렉션(Collection)
- 여러 개의 값을 모아서 한꺼번에 처리할 수 있는 자료형
1. 리스트(List) - 여러 개의 값을 집합적으로 모아서 저장, 가변적인 배열
- 인덱싱(indexing) - 인덱스를 통해 리스트의 값에 접근하는 방법
- 인덱스는 0번부터 1씩 증가하는 번호 (왼쪽에서 오른쪽으로 접근)
- 인덱스는 맨 뒤에서부터는 -1부터 1씩 감소하는 번호 (오른쪽에서 왼쪽으로 접근)
- 슬라이싱(slicing) - 인덱스를 사용하여 부분적으로 추출하는 방법
"""

# 리스트
a = [] # 빈 리스트
b = [1, 2, 3, 4, 5]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 3, 'python', True, 3.14]
# 이중 리스트
e = [1, 2, 3, ['Life', 'is', 'too', 'short']]

print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print(d)
print(type(d))
print(e)
print(type(e))
print("----------")

# 인덱싱
print(b[0])
print(b[2]) # 3
print(c[3]) # short
print(d[4]) # True
# 이중 리스트
print(e[3]) # ['Life', 'is', 'too', 'short']
print(e[-1]) # -1는 마지막 요소, ['Life', 'is', 'too', 'short']
print(e[3][3]) # short
print(e[-1][3]) # short
print(e[-1][-1]) # short
print(e[3][-1]) # short
print(e[-2]) # 3
print(e[0] + e[1]) # 3
# print(e[4]) # error : 해당 인덱스는 존재하지 않음
print("----------")
# 삼중 리스트
a = [1, 2, 3, ['a', 'b', 'c', ["Life", "is", "too", "short"], 'd'], 4] # 삼중 리스트
print(a[3])
print(a[3][1])
print(a[3][3])
print(a[3][3][3])
print("----------")

# 슬라이싱(slicing) - 인덱스를 사용하여 부분적으로 추출하는 방법
a = [1, 2, 3, 4, 5]
print(a[0:2]) # [1, 2]
print(a[1:4]) # [2, 3, 4]
print(a)      # [1, 2, 3, 4, 5]
print(a[0:5]) # [1, 2, 3, 4, 5]
print(a[0:])  # [1, 2, 3, 4, 5], 처음부터 끝까지
print(a[:])   # [1, 2, 3, 4, 5], 처음부터 끝까지
print(a[2:])  # [3, 4, 5], 2번부터 끝까지
print(a[:3])  # [1, 2, 3], 처음부터 3번 앞까지
print(a)
b = a[1:4] # [2, 3, 4], 슬라이싱하여 저장
print("b = ", b)
print("----------")

a = [1, 2, 3, ['a', 'b', 'c', 'd', 'e'], 4, 5]
print(a[2:5])   # [3, ['a', 'b', 'c', 'd', 'e'], 4]
print(a[3])     # ['a', 'b', 'c', 'd', 'e']
print(a[3][:3]) # ['a', 'b', 'c']
print("----------")

# 리스트 연산 - 리스트끼리 연산
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b) # 리스트 연결
c = a + b
print(c)
print(type(c))
print(a * 3) # 리스트 반복
d = a * 3
print(d)
# print(a * b) # error, a를 b번 반복할 수 없음
# print(a - b) # error
# print(a * 'hi') # error
print(a * b[0]) # a를 4번 반복
# print(a[2] + 'hi'); # error, 타입의 불일치

# 리스트의 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print("----------")

# 리스트 요소의 값 수정
a[0] = 7 
print(a)

# 리스트 요소의 값 삭제 - del() 함수 사용
a = [1, 2, 3, 4, 5, 6, 7]
del(a[0]) # 한 개 요소 삭제
print(a)  # [2, 3, 4, 5, 6, 7]

del a[0]  # 한 개 요소  삭제
print(a)  # [3, 4, 5, 6, 7]

del a[1:3]# 여러 개의 요소 삭제
print(a)  # [3, 6, 7]

del a[1:] # 1번 끝까지 삭제
print(a)  # [3]

