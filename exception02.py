# 2021/01/27(수)

'''
< 예외의 종류 >
SyntaxError - 문법적인 오류
TypeError - 연산 또는 함수의 자료형이 일치하지 않을 때 발생하는 오류
ValueError - 연산 또는 함수의 값이 부적할 때 발생하는 오류
NameError - 이름이 없을 때 발생하는 오류

ArithmeticError - ZeroDivisionError, OverflowError, FloatingPointError의 상위 클래스
ZeroDivisionError - 0으로 나눌때 발생하는 오류
IndexError - 시퀀스에서 인덱스의 범위를 벗어났을 때 발생하는 오류
IOError - 입출력 오류
FileNotFoundError - 실행하려고 하는 파일이 없을 때 발생하는 오류
RuntimeError - 실행시간에 발생하는 오류
'''

'''
# 1. FileNotFoundError
f = open('test.txt', 'r')
lines = f.readlines()

# 2. TypeError
a = 10
b = 'python'
c = a + b

# 3. NameError
a = 3
c = a + b
'''

'''
# 예외 회피 - 예외에 대한 확인이나, 처리를 하지 않고 다음으로 진행하게 하는 방법
# 예제) test.txt가 있다면 읽어서 처리하고, 이 후의 작업을 처리
# test.txt가 없다면 건너뛰고, 이 후의 작업을 처리
try:
    f = open('test.txt', 'r')
except:
    pass
    
f = open('test.txt', 'a')
f.write('Hello Python')
f.close()
'''
'''
# try: ~ except: ~ else: ~ 구문
# else절 : 예외가 발생하지 않을 때 처리 할 내용을 기술하는 절
# 예제) 첫번째 숫자를 두번째 숫자로 나누었을 때, 두번째 숫자가 0이 아닐때는 정상처리, 0일 때는 예외처리
a = int(input('정수 a 입력 : '))
b = int(input('정수 b 입력 : '))

try:
    c = a / b
except:
    c = a
    print(c)
    print('정상적으로 처리되지 않았습니다.')
else:
    print(c)
    print('정상적으로 처리되었습니다.')
'''
'''
# try 구문에 구조
try: 
    예외가 발생할 수 있는 구문, 필수
except:
    예외가 발생했을 때에 대한 처리 구문, 필수
else:
    예외가 발생하지 않고, 정상적으로 처리되었을 때에 대한 처리 구문, 선택
finally:
    예외의 발생 유무와 상관없이 항상 실행되는 구문, 선택
'''

# raise : 고의로 예외를 발생시킬 때 사용
# 예제) 양의 정수를 주면 1부터 해당 정수까지 1씩 누적하는 함수
# 음수를 사용할 수 없는 함수

'''
# -10을 매개변수를 받았을 때도 정상처리 -> 문제점
def add(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
'''

'''
# -10을 매개변수로 받았을 때 예외를 발생시킴 -> 해결
def add(n):
    if n < 0: raise ValueError    
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

try:
    #print(add(10))
    print(add(-10))
except ValueError:
    print('음수를 입력할 수는 없습니다.')
'''

'''
# 1번
class Bird:
    def fly(self):
        pass

class Eagle(Bird):
    pass
'''
'''
# 2번
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        return '먹이감을 찾아서 날고 있습니다.'
'''

'''
# 3번
#from abc import *
#from abc import ABCMeta, abstractmethod
import abc

class Bird(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fly(self):
        pass

class Eagle(Bird):
    def fly(self):
        return '먹이감을 찾아서 하늘 높이 하늘을 날고 있습니다.'
    
# b = Bird()
e = Eagle()
print(e.fly())
'''

# 문제) 찾는 단어가 없을 때의 처리를 예외처리 사용해 보시오.
dic = {'boy':'소년', 'school':'학교', 'book':'책'} 




























