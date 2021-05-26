# 2021/01/07(목)

# 리스트 활용
s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(s)
print(s[3])    # 인덱싱
print(s[1:5])  # 슬라이싱
print(s[:])    # 처음부터 끝까지, 기본 1칸씩 출력
print(s[::2])  # 처음부터 끝까지, 2칸씩 건너뛰며 출력
print(s[::3])  # 처음부터 끝까지, 3칸씩 건너뛰며 출력
print(s[::-1]) # 끝에서부터 처음까지

# 문자열 활용
s = "일월화수목금토"
print(s)
print(s[3])    # 인덱싱
print(s[1:6])  # 슬라이싱
print(s[:])    # 처음부터 끝까지, 기본 1칸씩 출력
print(s[::2])  # 처음부터 끝까지, 2칸씩 건너뛰며 출력
print(s[::3])  # 처음부터 끝까지, 3칸씩 건너뛰며 출력
print(s[::-1]) # 끝에서부터 처음까지

#####
# 리스트의 참조와 복사
a = [1, 2, 3]
b = a # 참조만 대입, 복사된 것이 아님.
print(a)
print(b)

# a와 b는 같은 리스트인가? 복사된것인가?
# 1번 방법 - 값 1개를 변경
a[1] = 4
print(a)
print(b)

# 2번 방법 - 메모리의 주소 확인
print(id(a)) # 2142149933312
print(id(b)) # 2142149933312

# 3번 방법 - is 연산자, is not 연산자
c = [1, 4, 3]
print(a is b) # 객체가 같은 것인가?
print(a is c)
print(a == b) # 내용이 같은 것인가?
print(a == c)
print(a is not b) # 객체가 다른 것인가?
print(a is not c)
print("----------")

#####
# 내용을 복사 - copy 모듈 사용
from copy import copy
a = [1, 2, 3]
b = copy(a)

print(a)
print(b)

# 1. 메모리의 주소 확인 - 다른 주소
print(id(a)) # 1951629678976
print(id(b)) # 1951662624384

# 2. 값 1개 변경
a[1] = 4
print(a)
print(b)

# 3. is 연산자로 비교
print(a is b)
print(a is not b)
print(a == b)
print("----------")

# 변수를 생성하는 방법
'''
# 1번
a = "python"
b = "python"

# 2번
a = "python"; b = "python"

# 3번
a = b = "python"
print(a); print(b)
'''
# 2개의 변수 선언
a = "python"; b = "java"
a, b = "python", "java"
(a, b) = ("python", "java")
[a, b] = ["python", "java"]

print(a)
print(b)
print("----------")

# 2개의 변수 값 서로 바꾸기
# swapping
a, b = b, a

print(a)
print(b)









































































