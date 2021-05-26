# 2021/0122(금)

'''
< 상속 >
mro - method resolution order, 메소드 실행 순서, 메소드를 확인하는 순서
__mro__ 속성 : 메소드를 실행하는 순서를 확인할 수 있음.
- 파이썬은 다중상속을 허용하는데,
- 문제점 : 생성자를 직접호출하면 생성자 호출이 중복되는 문제가 발생
- 해결책 : super()를 통해서 생성자를 호출함.

'''
'''
# 예제1) 
class A:
    def __init__(self):
        super().__init__()
        print('A 클래스')

class B:
    def __init__(self):
        super().__init__()
        print('B 클래스')

class C(B, A):
    def __init__(self):
        super().__init__()
        print('C 클래스')
    

c = C()
print(C.__mro__)
'''

# 예제2)
'''
# 문제점 : 부모의 생성자를 직접 호출할 때의 문제점
# - 생성자를 직접호출하게 되면 A 클래스가 2번 호출하게 됨.
class A:
    def __init__(self):
        print('A 클래스')

class B(A):
    def __init__(self):
        print('B 클래스')
        A.__init__(self)

class C(A):
    def __init__(self):
        print('C 클래스')
        A.__init__(self)

class D(B, C):
    def __init__(self):
        print('D 클래스')
        B.__init__(self)
        C.__init__(self)

d = D()
print(D.__mro__)

'''
'''
# 해결책 : super()를 사용하여 부모의 생성자를 호출.
# - A 클래스를 한번만 출력하게 됨.
class A:
    def __init__(self):
        print('A 클래스')

class B(A):
    def __init__(self):
        print('B 클래스')
        super().__init__()

class C(A):
    def __init__(self):
        print('C 클래스')
        super().__init__()

class D(B, C):
    def __init__(self):
        print('D 클래스')
        super().__init__()      

d = D()
print(D.__mro__)
'''

# 문제1) 아래의 클래스를 상속관계로 정의하고, 인스턴스를 생성하여 확인하시오.
# 부모 클래스 : Person, 멤버변수 : name, age, job
# Person의 자식 클래스 : Employee, 멤버변수 : company, salary
# Person의 자식 클래스 : Student, 멤버변수 : school

# 정답1)
'''
class Person:
    def __init__(self, name, age, job=None):
        self.name = name
        self.age = age
        self.job = job
    def __str__(self):
        if self.job is 'Employee':
            return '{}({}, {}, {}, {})'.format('Employee', self.name, self.age, self.company, self.salary)
        elif self.job is 'Student':
            return '{}({}, {}, {})'.format('Student', self.name, self.age, self.school)
        else:
            return '{}({}, {})'.format('Person', self.name, self.age)
        
class Employee(Person):
    def __init__(self, name, age, company, salary):
        super().__init__(name, age, 'Employee')
        self.company = company
        self.salary = salary

class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age, 'Student')
        self.school = school

e = Employee('이익준', 41, '을제병원 감담췌외과', 8000)
print(e)

s = Student('강예서', 19, '신아고등학교')
print(s)

p = Person('전유진', 16)
print(p)
'''
'''
# 정답2)
class Person:
    def __init__(self, name, age, job='Person'):
        self.name = name
        self.age = age
        self.job = job
    def __str__(self):
        return '{} : {}, {}'.format(self.job, self.name, self.age)
        
class Employee(Person):
    def __init__(self, name, age, company, salary):
        super().__init__(name, age, 'Employee')
        self.company = company
        self.salary = salary
    # 오버라이딩
    def __str__(self):
        return super().__str__() + ', {}, {}'.format(self.company, self.salary)
    

class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age, 'Student')
        self.school = school
    # 오버라이딩
    def __str__(self):
        return super().__str__() + ', {}'.format(self.school)

e = Employee('이익준', 41, '을제병원 감담췌외과', 8000)
print(e)

s = Student('강예서', 19, '신아고등학교')
print(s)

p = Person('전유진', 16)
print(p)
'''

# < 과제 >
# 상속 관계를 설정하고, 아래의 두 클래스를 생성하고 확인하시오.
# 부모 클래스 - Car, 멤버변수: name, color, gear, seat
# Car의 자식 클래스 - SuperCar, Sedan, Truck
# SuperCar : gear는 'manual'이 기본이고, seat수는 2개를 기본값으로 설정, turbo 기능 추가.
# Sedan : gear는 'auto'이 기본이고, seat수는 5개를 기본값으로 설정. comfort 기능 추가
# Truck : gear는 'auto'이 기본이고, seat수는 2개를 기본값으로 설정, load(짐 싣는) 기능추가

class Car:
    def __init__(self, name, color, gear, seat):
        self.name = name
        self.color = color
        self.gear = gear
        self.seat = seat
    def __str__(self):
        return '이름: {}, 색상: {}, 기어: {}, 시트: {}개'.format(self.name, self.color, self.gear, self.seat)

class SuperCar(Car):
    def __init__(self, name, color, gear='manual', seat=2):
        super().__init__(name, color, gear, seat)
    def turbo():
        print('슈퍼카는 터보 기능이 있습니다.')

class Sedan(Car):
    def __init__(self, name, color, gear='auto', seat=5):
        super().__init__(name, color, gear, seat)
    def comfort():
        print('세단은 편안하게 주행합니다.')

class Truck(Car):
    def __init__(self, name, color, gear='auto', seat=2):
        super().__init__(name, color, gear, seat)
    def load():
        print('트럭은 짐을 싣을 수 있습니다.')

c1 = Car('아반떼', '흰색', 'auto', 4)
print(c1)
c2 = SuperCar('페라리', '빨강색')
print(c2)
c3 = Sedan('롤스로이스', '검정색')
print(c3)
c4 = SuperCar('봉고3', '파랑')
print(c4)
print('----------')

# 다형성 구현
cars = [c1, c2, c3, c4]
for c in cars:
    print(c)

