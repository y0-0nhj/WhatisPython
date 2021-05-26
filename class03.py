# 2021/010/19(화)

'''
< 클래스 >
변수의 구분
1. 인스턴스 변수 : 인스턴스마다 생성되어 각 인스턴스가 갖는 변수, self를 붙여 사용하는 변수
2. 클래스 변수 : 인스턴스에 소속된 것이 아니라, 딱 1개만 생성되어 클래스 전체에서 공유하는 변수, cls를 붙여 사용하는 변수

메소드의 구분
1. 인스턴스 메소드 : 각 인스턴스에 소속되어 인스턴스 변수를 처리하는 메소드
2. 클래스 메소드 : 딱 1개만 생성되어 클래스 전체에서 공유하는 메소드, @classmethod라는 데코레이터를 붙여서 생성함.
3. 정적 메소드 : 클래스 포함된 단순한 메소드, self나 cls를 사용하지 않음. 객체와 관련된 동작을 하지는 않음.
- 정적 메소드는 @staticmethod라는 데코레이션을 붙여서 작성함.
'''

'''
class Car:
    count = 0 # 클래스 변수 선언
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price
        Car.count += 1
        self.no = Car.count

    @classmethod 
    def printcount(cls): # 클래스 메소드
        return cls.count

    def printinfo(self):
        print('No {0}.\n차이름: {1}\n차모델: {2}\n차가격: {3}\n'.format(self.no, self.name, self.model, self.price))

    @staticmethod
    def sayhello(): #정적 메소드
        return '오늘도 안전하게 작업하도록 합시다.'

car1 = Car('sonata', '중형', 3000)
car2 = Car('k9', '대형', 7000)
car3 = Car('gv70', 'SUV', 8000)

car1.printinfo()
car2.printinfo()
car3.printinfo()

print(Car.sayhello())
print('생산된 자동차의 수 : {0}'.format(Car.printcount()))  # 권장되는 방법
print('생산된 자동차의 수 : {0}'.format(car1.printcount())) # 권장되지 않는 방법
'''

##########
'''
클래스 안에서 사용되는 연산자 메소드, 특수 메소드
__aaa__

'''



































































































































