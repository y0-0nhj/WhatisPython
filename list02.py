# 2021/01/04(월)

"""
리스트 관련 함수

1. 리스트에 값을 추가
- append() - 리스트에 맨 뒤에 값을 추가하는 방법
- insert() - 리스트의 해당하는 인덱스에 값을 추가하는 방법


2. 리스트의 값을 삭제
- remove() - 값을 찾아 삭제 
- pop() - 맨 마지막 요소의 값을 삭제
- pop(x) - 해당하는 요소의 인덱스의 값을 삭제
- remove()의 리턴값은 None, pop()의 리턴값은 삭제되는 요소의 값.

"""
# 리스트에 맨 뒤에 요소 추가 - append() 함수
a = [1, 2, 3, 4, 5] # 0 ~ 4번 인덱스
#a[5] = 6 # error, 없는 인덱스에 값의 대입은 불가능
print(a)
print('a의 길이: ', len(a))

a.append(6) # 한 개 요소 추가
print(a)
print('a의 길이: ', len(a))

#a.append(7, 8, 9) # 에러 - 한번에 여러 개의 요소 추가 불가

a.append([7, 8, 9]) # 리스트를 하나의 요소로 추가
print(a)
print('a의 길이: ', len(a))
print("----------")

# 중간에 요소 추가 - insert() 함수 : None을 리턴
a = [1, 2, 3, 4, 5]
print(a)

a.insert(2, 6)
print(a) # [1, 2, 6, 3, 4, 5]

# 요소 삭제 - remove() 함수
print(a.remove(2)) # [1, 6, 3, 4, 5], 2라는 값을 삭제, 인덱스가 아님.
print(a)

# 요소 삭제 - pop() 함수 : 삭제되는 값을 리턴
# pop() 함수의 2가지 사용법
# 1. pop()  - 맨 마지막 인덱스의 값을 삭제
# 2. pop(x) - 해당하는 인덱스의 값을 삭제

print(a.pop())
print(a)

print(a.pop(1))
print(a)
print("----------")

# 리스트 정렬
a = [2, 4, 1, 5, 3]
print(a)
# a.sort() # 오름차순 정렬
a.sort(reverse=True) # 내림차순 정렬
print(a)

# 리스트 뒤집기
a = ['Life', 'is', 'too', 'short']
a.reverse()
print(a)

# 리스트의 값에 대한 인덱스 확인
a.reverse()
print(a)
print(a.index("too"))

# 리스트 문자열 정렬 - 대소문자 구분해서 정렬
a.sort() # 오름차순
print(a)

a.sort(reverse=True)
print(a)

a.sort(key=str.lower) # 대문자를 소문자로 취급하여 정렬함
print(a)
print("----------")

# 값이 포함된 갯수 구하기
a = [1, 2, 3, 4, 5, 1, 1, 2]
print(a.count(1))
print(a.count(2))
print(a.count(5))
print(a.count(6))

# 리스트의 확장
a = [1, 2, 3]
print(a)
#a.append(4, 5) # error
#a.append([4, 5]) # [1, 2, 3, [4, 5]]

'''
b = [4, 5]
a = a + b
위의 두 줄을 한번에 처리하는 방법 -> 리스트의 확장
'''
# 복합대입 연산자, 결합 연산자, 할당 연산자
# +=, -=, *=, /= ...
# a = a + [4, 5]
a += [4, 5]
# a.extend([4, 5]) # [1, 2, 3, 4, 5]
print(a)


