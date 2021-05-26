# 2020/12/31(목)
# 연산자

"""
자바   : &&   ||  !
오라클 : and  or  not
R     :  &    |   !
파이썬 : and  or  not
"""


"""
< 연산자의 종류 >
1. 대입 연산자 : =
2. 산술 연산자 : +, -, *, /(소숫점을 포함한 나눈 결과)
//(나누기의 몫), %(나누기의 나머지), **(승수)
3. 비교 연산자 : >, >=, <, <=, ==, !=
- 비교 연산의 결과는 반드시 True 또는 False 
4. 논리 연산자 : and, or, not
- 논리 연산의 결과는 반드시 True 또는 False
- 비교가 논리보다 우선순위가 높음
5. 부호 연산자 : +, -  ex) +10, -10
6. 비트 연산자 : &(비트 and), |(비트 or), ~(비트 not), ^(XOR, exclusive or)
7. 쉬프트 연산자 : <<, >> (비트로 이동)

"""

a = 10
b = 3
# 산술 연산자
print("a + b = ", a+b)
print("a - b = ", a-b)
print("a * b = ", a*b)
print("a / b = ", a/b)   # 나눈 결과 출력, 3.3333333333333335
print("a // b = ", a//b) # 몫, 3
print("a % b = ", a%b)   # 나머지, 1
print("3 ** 4 = ", 3**4) # 승수, 3의 4승, 81
print()

# 비교 연산자
print("a > b : ", a>b)
print("a < b : ", a<b)
print("a == b : ", a==b)
print("a != b : ", a!=b)
print()

# 논리 연산자
# a = 10, b = 3
print(a > 5 and b < 5)
print(a > 5 and b > 5)
print(a < 5 and b > 5)
print(a > 5 or b < 5)
print(a > 5 or b > 5)
print(a < 5 or b > 5)
print(a > b)
print(not(a > b))
print()

# 비트 연산자
x = 0b1101 # 10진수 13
y = 0b1011 # 10진수 11
print(x & y) # 1001 -->  9
print(x | y) # 1111 --> 15
print(x ^ y) # 0110 -->  6
print()

# 쉬프트 연산자
x = 0b00000010 # 2
print(x << 3) # 00010000 --> 16, 2진수의 곱셈
y = 0b00100000 # 32
print(y >> 3) # 00000100 --> 4 , 2진수의 나눗셈
print()

# 변환 함수 - int(), float(), str()
# 참과 거짓을 판별하는 함수 - bool()
# 반올림 함수 - round()
n1 = 10
n2 = "20"
n3 = 23.4
n4 = "55.5"
n5 = str(n3)
print(n1 + int(n2))
print(n3 + float(n4))
print(type(n3))
print(type(n5))

n6 = ""
n7 = 0
n8 = None
print(bool(n1))
print(bool(n6))
print(bool(n7))
print(bool(n8))
print()

a = 1234.5678
print(a)
print(round(a))     # 1235, 일의 자리까지 반올림
print(round(a, 2))  # 1234.57, 소숫점 둘째자리까지 반올림
print(round(a, -1)) # 1230.0, 십의 자리까지 반올림
print(round(a, -2)) # 1200.0, 백의 자리까지 반올림



