# 2021/01/21(목)

# module03.py를 모듈로 불러와서 사용
from module03 import *

# 변수 사용
print('원주율 : {0}'.format(PI))

# 함수 사용
print('덧셈 : {0}'.format(add(7, 8)))

# 클래스 사용 - 인스턴스 생성
c = Circle()

print('원의 면적 : {0:0.2f}\n원의 둘레 : {1:0.2f}'.format(c.setarea(5.5), c.setperi(5.5)))




