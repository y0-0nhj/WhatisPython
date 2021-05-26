# 2021/01/20(수)

'''
< 연산자 오버로딩(operator overloading) >
- 기본형 데이터가 아닌 객체형 데이터에 대해서도 연산자를 사용하여 계산하도록 하는 것.
- 연산자 함수를 만들어두고, 사용은 연산자로 함.
< 연산자 함수 >
- 연산자 오버로딩을 하기 위해 생성하는 함수

< 클래스 내부에서 사용하는 특수한 함수 >
1. __str__
2. __getitem__
3. __setitem__

< 유틸리티 모듈 >
fractions 모듈 - 수학에서처럼 분수를 다룰 수 있도로 하는 모듈

'''

'''
class Point:
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y
    # 연산자 함수(+)
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    # 연산자 함수(-) : __sub__
    # 연산자 함수(*) : __mul__, Point*정수
    # 연산자 함수(/) : __truediv__, Point/정수
    # 연산자 함수(!=) : __ne__
     
p1 = Point(10, 20)
p2 = Point(30, 40)
p3 = Point(10, 20)

print(p1)
print(p2)
print(p3)
print(id(p1))
print(id(p2))
print(id(p3))
p1.show()
p2.show()
p3.show()
print('----------')
print(p1 == p2)
print(p1 == p3) # 연산자, False -> 연산자함수를 사용한 후 True
print(p1.__eq__(p3)) # 연산자 함수
print('----------')
print(p1.compare(p2))
print(p1.compare(p3))

p4 = p1 + p2 # 연산자
p4.show() 
p4 = p1.__add__(p2) # 연산자 함수
p4.show()
'''

# 예제1)
'''
class Member:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    # 출력함수 : 함수 호출
    def show(self):
        return ('{0}({1})'.format(self.id, self.name))
    # 출력함수 : 자동 호출이 되도록 정의
    def __str__(self):
        return ('{0}({1})'.format(self.id, self.name))

m1 = Member('aaa1234', '이익준')
print(m1.show())
print(m1) # __str__ 함수를 자동호출
'''

'''
# 예제2) 딕셔너리로 저장하는 클래스
class Member:
    def __init__(self, id='', name=''):
        self.info = {'id':id, 'name':name}

    def __getitem__(self, data):
        return self.info[data]

    def __setitem__(self, id, name):
        self.info[id] = name


m1 = Member('aaa1234', '이익준')
print(m1.info)
# __getitem__ 사용
print(m1['id'])
print(m1['name'])

m2 = Member()
# __setitem__ 사용
m2['id'] = 'bbb3333'
m2['name'] = '김준완'
print(m2.info)
'''

# < 모듈을 사용하는 방법 >
'''
# 1번 방법
import fractions
a = fractions.Fraction(1, 3) # Fraction(분자, 분모)
b = fractions.Fraction(3, 4)
print(a)  # 1/3
a = a + 1
print(a)  # 4/3
print(1/3) # 0.3333333333333333
print(a + b) # 4/3 + 3/4 => 24/12
'''

'''
# 2번 방법
import fractions as f
a = f.Fraction(1, 3)
b = f.Fraction(3, 4)
print(a + b)
'''

# 3번 방법 - 가장 많이 사용
# - 모듈 안의 모든 함수를 함수이름으로 바로 사용할 수 있도록 하는 방법
# - 마치 내장함수처럼 사용하는 방법
#from fractions import * # 모든 함수에 대해서
from fractions import Fraction # Fraction() 함수에 대해서
a = Fraction(1, 3)
b = Fraction(3, 4)
print(a + b)



