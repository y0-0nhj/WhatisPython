# 2021/01/21(목)

# < 과제 >
# 상속 관계를 설정하고, 아래의 두 클래스를 생성하고 확인하시오.
# 부모 클래스 - Car, 멤버변수: color, gear, seat
# 자식 클래스 - SuperCar, Sedan, Truck
# SuperCar : gear는 '수동'이 기본이고, seat수는 2개를 기본값으로 설정, turbo 기능 추가.
# Sedan : gear는 '자동'이 기본이고, seat수는 5개를 기본값으로 설정. comfort 기능 추가
# Truck : gear는 '자동'이 기본이고, seat수는 2개를 기본값으로 설정, load(짐 싣는) 기능추가

'''
< 상속 >
mro - method resolution order, 메소드 실행 순서, 메소드를 확인하는 순서
__mro__ 속성 : 메소드를 실행하는 순서를 확인할 수 있음.
- 파이썬은 다중상속을 허용하는데, 왼쪽에 있는 부모클래스의 생성자를 실행

'''

'''
# 예제1) 
class A:
    def __init__(self):
        print('A 클래스')

class B:
    def __init__(self):
        print('B 클래스')

class C(A, B):
    def __init__(self):
        super().__init__()
        print('C 클래스')
    

c = C()
print(C.__mro__)
'''




















































