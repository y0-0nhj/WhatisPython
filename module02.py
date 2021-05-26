# 2021/01/21(목)

'''
module02.py에서 module01.py파일의 사칙연산 함수를 사용

'''
# 1번 방법
import module01

print(module01.add(10, 20))
print(module01.sub(30, 7))
print(module01.mul(5, 3))
print(module01.div(10, 3))
print('----------')

# 2번 방법
import module01 as m
print(m.add(5, 7))
print(m.sub(20, 7))
print(m.mul(7, 6))
print(m.div(30, 4))
print('----------')

# 3번 방법
from module01 import *
print(add(8, 7))
print(sub(9, 5))
print(mul(8, 6))
print(div(10, 4))












