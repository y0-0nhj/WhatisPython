# 2021/01/19(화)

# < 확인학습 > - 클래스
# 문제1) 과일이름, 과일수량, 과일가격, 할인율, 판매가를 멤버로 가지는 클래스 Fruit를 생성하시오.
# 과일의 정보를 출력하는 메소드를 만들어서 학인하시오.

# 문제2) 회원이름, 아이디, 나이, 기본 혜택을 멤버로 가지는 클래스 Member를 생성하시오.
# 회원의 정보를 출력하는 메소드를 만들어서 확인하시오.

# 문제3) 학번, 이름, 국어점수, 수학점수, 학점을 멤버로 가지는 클래스 Student를 생성하시오.
# 학생의 정보를 출력하는 메소드를 만들어서 확인하시오.
'''
# 클래스 정의
class Fruit:
    # 생성자 : 이름, 수량, 가격, 할인율, 판매가
    def __init__(self, name, volume, price, rate):
        self.name = name 
        self.volume = volume
        self.price = price
        self.rate = rate
        self.price2 = price - price*rate 

    def showinfo(self):
        print('이름: {0}\n수량: {1}\n정가: {2}\n할인율: {3}\n판매가: {4}\n'
              .format(self.name, self.volume, self.price, self.rate, self.price2))

# 인스턴스 생성
apple = Fruit('사과', 250, 1500, 0.1)
mango = Fruit('망고', 120, 2000, 0.2)

print('### 과일 정보 출력 ###')
apple.showinfo()
mango.showinfo()
'''
# 예제) 4칙 연산을 하는 계산기
# 숫자 2개를 가지고 덧셈, 뺄셈, 곱셈, 나눗셈을 하는 프로그램을 클래스로 작성하고 인스턴스를 생성하여 확인하시오.
# 클래스 이름은 Calculator로 설정하시오.
'''
# 클래스 정의
class Calculator:
    # 생성자 : 두 개의 값을 설정
    # 메소드를 통해서 4칙 연산을 하도록 설정
    # 설정 메소드 : 두 개의 값의 다시 설정
    
    def __init__(self, first=0, second=0): # 디폴트 매개변수
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def subtract(self):
        result = self.first - self.second
        return result

    def multiply(self):
        result = self.first * self.second
        return result

    def divide(self):
        result = self.first / self.second
        return result

# 인스턴스 생성
c1 = Calculator()
c1.setdata(30, 10)
print(c1.add())

c2 = Calculator(10, 5)
print(c2.multiply())
'''

# 예제) 년, 월, 일을 갖는 날짜 클래스를 작성하고, 인스턴스를 만들어 확인하시오.
# 클래스 정의
# 액세소(accessor) - getter, setter

'''
# version 1
class Date:
    def __init__(self, year=1, month=1, day=1):
        self.year = year
        self.month = month
        self.day = day

    # setter 메소드
    def setDate(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def setyear(self, year):
        self.year = year

    def setmonth(self, month):
        self.month = month

    def setday(self, day):
        self.day = day

    # getter 메소드 
    def printDate(self):
        print('{0}년 {1}월 {2}일'.format(self.year, self.month, self.day))

# 인스턴스 생성
date1 = Date(2021, 2, 12)
date1.printDate()
print('----------')
'''

# 객체지향의 특징 - 캡슐화, 상속, 다형성
# 문제점 : 캡슐화의 관점에서 보면 멤버변수는 외부에서 접근 불가, setter/getter 메소드를 통해서 접근 가능
# 해결책 : property(프로퍼티)를 사용
# 1. 멤버변수의 이름을 어렵게 만든다.

'''
# version 2 - property 사용
class Date:
    def __init__(self, year=1, month=1, day=1):
        self.inner_year = year
        self.inner_month = month
        self.inner_day = day

    # setter 메소드
    def setDate(self, year, month, day):
        self.inner_year = year
        self.inner_month = month
        self.inner_day = day

    def setyear(self, year):
        self.inner_year = year

    def setmonth(self, month):
        self.inner_month = month

    def setday(self, day):
        self.inner_day = day

    # getter 메소드
    def getyear(self):
        return self.inner_year

    def getmonth(self):
        return self.inner_month

    def getday(self):
        return self.inner_day

    # 프로퍼티(property) - getter/setter를 통해서 멤버변수의 값에 접근하도록 함.
    month = property(getmonth, setmonth)

    # 출력 메소드    
    def printDate(self):
        print('{0}년 {1}월 {2}일'.format(self.inner_year, self.inner_month, self.inner_day))

date2 = Date()
date2.month = 2    # 프로퍼티 사용 - 내부적으로 setmonth() 사용
print(date2.month) # 프로퍼티 사용 - 내부적으로 getmonth() 사용

'''

'''
# version 3 - property(프로퍼티), decorator(데코레이터) 사용
# @ : 데코레이터
# 데코레이터 : 프로퍼티의 선언과 getter/setter 메소드를 하나로 표현
class Date:
    def __init__(self, year=1, month=1, day=1):
        self.inner_year = year
        self.inner_month = month
        self.inner_day = day

    @property # get 프로퍼티 : getter 메소드
    def year(self):
        return self.inner_year

    @year.setter  # set 프로퍼티 : setter 메소드
    def year(self, year):
        self.inner_year = year
    
    @property # get 프로퍼티 : getter 메소드 
    def month(self):
        return self.inner_month

    @month.setter # set 프로퍼티 : setter 메소드
    def month(self, month):
        self.inner_month = month

    @property # get 프로퍼티 : getter 메소드 
    def day(self):
        return self.inner_day

    @day.setter # set 프로퍼티 : setter 메소드
    def day(self, day):
        self.inner_day = day

    # 출력 메소드
    def printdate(self):
        print('{0}년 {1}월 {2}일'.format(self.inner_year, self.inner_month, self.inner_day))

date2 = Date()
date2.printdate()

# date2.setmonth(2) -> 없으니까 에러
date2.month = 2
print('월:', date2.month)
date2.printdate()

date2.year = 2021
date2.printdate()

date2.day = 12
date2.printdate()

# 문제점) 멤버변수의 이름을 안다면 접근 가능함
date2.inner_year = 1492
date2.printdate()
print('----------')
'''

# version 4 - property(프로퍼티), decorator(데코레이터) 사용
# @ : 데코레이터
# 데코레이터 : 프로퍼티의 선언과 getter/setter 메소드를 하나로 표현
# 멤버변수이름을 숨기는 방법: 멤버변수 이름 앞에 __을 붙여서 만듦.
# __(언더바 2개)를 붙여 멤버변수 이름을 만들면 실제 멤버변수 이름은 _클래스명__변수명이 됨.
# ex) Date 클래스의 __year -> 접근할때는 _Date__year이라고 사용함.
class Date:
    def __init__(self, year=1, month=1, day=1):
        self.__year = year
        self.__month = month
        self.__day = day

    # get 프로퍼티 : getter 메소드
    @property
    def year(self):
        return self.__year

    @property 
    def month(self):
        return self.__month

    @property 
    def day(self):
        return self.__day

    '''
    # set 프로퍼티 : setter 메소드
    @year.setter  
    def year(self, year):
        self.__year = year

    @month.setter 
    def month(self, month):
        self.__month = month

    @day.setter 
    def day(self, day):
        self.__day = day
    '''

    # 출력 메소드
    def printdate(self):
        print('{0}년 {1}월 {2}일'.format(self.__year, self.__month, self.__day))

date2 = Date()
date2.printdate()

# date2.year = 2021 # set 프로퍼티가 없으면 에러 발생
# date2.__year = 2021 # 멤버변수인 __year에 값이 설정되지 않음
date2._Date__year = 2021
date2.printdate()









