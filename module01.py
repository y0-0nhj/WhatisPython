# 2021/01/21(목)

'''
모듈(module) - 함수, 변수, 클래스를 모아 놓은 파일

< 모듈을 사용하는 방법 >
1. import 모듈명
import array
array.array() # array() 함수 사용

2. import 모듈명 as 별칭
import array as a
a.array() # array() 함수 사용

3. from 모듈명 import 함수명
from array import * # array 모듈의 모든 함수 사용
from array import array # array() 함수만 사용
array() # array() 함수 사용


# 해당 파일이 다른 파일에서 모듈로 사용된다면 
# 실행문을 적을 때 if __name__ == '__main__':  안에서 테스트를 한다.

'''

# 사칙 연산을 하는 함수
# module01.py 파일로 저장 -> 모듈로 저장
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

# 지금 모듈(파일)에서만 실행.
# 다른 파일에서 이 모듈을 불러와서 사용할 때는 실행되지 않음.
if __name__ == '__main__':  
    print(add(333, 444))
    print(sub(550, 330))






