# 2021/01/04(월)

'''
() - 소괄호 : parentheses, brackets
{} - 중괄호 : braces
[] - 대괄호 : square brackets

'''

"""
튜플(tuple) - 몇가지의 특징을 제외하면, 리스트의 거의 흡사한 데이터 타입
- 리스트는 []를 사용하지만, 튜플은 ()를 사용
- 리스트는 수정/삭제가 가능하지만, 튜플은 한번 설정된 값의 변경이 불가(수정/삭제 불가)

튜플의 사용되는 경우 - 한 번 설정하면, 값의 변경이 발생되지 않는 상황에서 사용 가능.
대개의 경우는 값이 변경이 자주 일어나므로 리스트를 많이 사용함.
"""

t1 = () # 빈 튜플
t2 = (1, 2, 3)
t3 = 1, 2, 3
t4 = (1, 2, 3, ('a', 'b', 'c'), 4, 5)

print(t1)
print(type(t1))
print(t2)
print(type(t2))
print(t3)
print(type(t3))
print(t4)
print(type(t4))

# 튜플에 추가, 수정, 삭제는 불가능
# t2.append(10) # 추가 불가
# t2.remove(2)  # 삭제 불가
# del(t2[1])    # 삭제 불가
# t2[1] = 4     # 수정 불가   

# 인덱싱
print(t4[2])
print(t4[3])
print(t4[3][2])
print("----------")

# 슬라이싱
t5 = (1, 2, 3, 4, 5)
print(t5)
print(t5[:])
print(t5[:3])
print(t5[2:])
print(t5[2:4])

# 튜플 연산
t6 = (6, 7, 8)
print(t5 + t6) # 튜플 더하기
print(t5 * 3)  # 튜플 곱하기
print(len(t5))
print(len(t6))

t5 += (9, 10)  # 튜플에 값 추가
print(t5)
      
t5 = (1, 2, 3)
print(t5)
print("----------")

# 리스트와 튜플의 차이점
a = [10]  # list
b = (10)  # int
c = (10,) # tuple
d = 10,   # tuple

print(a)       # [10]
print(type(a)) # list
print(b)       # 10
print(type(b)) # int
print(c)       # (10,) 
print(type(c)) # tuple
print(d)       # (10,) 
print(type(d)) # tuple

# 튜플은 변경(수정/삭제) 불가
a = 1, 2, 3, 4, 5

print(a)
print(type(a))

# ba.sort()   # error - 변경 불가
# a.reverse() # error - 변경 불가


'''
딕셔너리 - 자바의 맵과 같은 구조
- key와 value를 쌍으로 가지는 구조

문자열 다루는 방법

'''

