# 2021/01/18(월)

'''
클래스 - 속성(멤버변수)과 동작(메소드)을 하나로 묶어서 객체를 정의하는 것

생성자 - __init__()
1. 생성시기 : 인스턴스가 만들어질 때 자동 호출
2. 목적 : 멤버변수의 값을 초기화

self
1. 자바의 this와 같은 기능
2. 자신의 멤버변수를 지칭하며, 매개변수와 구분하기 위해 사용
3. 생성자 및 메소드의 매개변수에서 첫번째에 적는다.
'''

# 예제) 이름과 나이의 데이터 가지고, 출력하는 클래스
# 속성 : 이름, 나이 변수
# 메소드 : 이름과 나이 데이터 출력하는 메소드

'''
class Person:
    # 생성자 - 멤버변수의 값을 초기화하는 목적    
    def __init__(self, name='', age=0): # 디폴트 매개변수
        self.name = name
        self.age = age

    # 출력 메소드
    def introduce(self):
        print('이름은 %s이고, 나이는 %d살입니다.' % (self.name, self.age))

    # setter 메소드
    def setname(self, name):
        self.name = name

    def setage(self, age):
        self.age = age

    def set(self, name, age):
        self.name = name;
        self.age = age;
    

# 인스턴스(객체) 생성
p1 = Person('이익준', 42)
p2 = Person()
p3 = Person('김준완')
p4 = Person('', 45)

# setter 메소드 호출
p2.set('채송화', 39)
p3.setage(41)
p4.setname('양석형')

# introduce 메소드 호출
p1.introduce()
p2.introduce()
p3.introduce()
p4.introduce()
'''

# 예제) 숫자 한 개씩을 계속 더하는 계산기 클래스
# 속성 : 값을 누적하는 변수
# 메소드 : 값을 누적하여 더하는 메소드

'''
class Calculator:
    # 생성자
    def __init__(self):
        self.result = 0

    # 덧셈 메소드
    def add(self, num):
        self.result += num
        return self.result

    # 출력 메소드
    def show(self):
        print('덧셈 결과는 {0}입니다.'.format(self.result))

# 인스턴스(객체) 생성
c1 = Calculator()
c1.add(5)
c1.add(7)
c1.add(8)
c1.show()
'''

# < 확인학습 > - 클래스
# 문제1) 과일이름, 과일수량, 과일가격, 할인율, 판매가를 멤버로 가지는 클래스 Fruit를 생성하시오.
# 과일의 정보를 출력하는 메소드를 만들어서 학인하시오.

# 문제2) 회원이름, 아이디, 나이, 기본 혜택을 멤버로 가지는 클래스 Member를 생성하시오.
# 회원의 정보를 출력하는 메소드를 만들어서 확인하시오.

# 문제3) 학번, 이름, 국어점수, 수학점수, 학점을 멤버로 가지는 클래스 Student를 생성하시오.
# 학생의 정보를 출력하는 메소드를 만들어서 확인하시오.






























