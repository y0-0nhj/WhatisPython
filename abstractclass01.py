# 2021/01/22(금)

'''
< 추상 클래스 (abstract class) >
1. 추상 메서드를 하나 이상 가지는 클래스.
2. 추상 클래스는 인스턴스를 생성할 수 없음.
3. 상속을 이용하여 다형성을 구현할 목적으로 사용함.
4. 추상 클래스를 생성하기 위해서는 abc 모듈의 ABCMeta 클래스, abstractmethod 메소드를 사용
5. 추상 클래스로부터 상속을 받은 클래스는 추상 클래스의 추상 메소드를 반드시 오버라이딩 해야 한다.
6. 오버라이딩하지 않으면 해당 클래스로 만들어야 한다.

< 추상 메소드 (abstract method) >
1. 내용이 없는 메소드
2. pass를 사용

'''


'''
from abc import ABCMeta, abstractmethod

class A(metaclass=ABCMeta): # 추상 클래스
    @abstractmethod   # 추상 메소드
    def display(self):
        pass

class B(A):
    #pass
    # 오버라이딩하면 인스턴스 생성 가능
    def display(self):
        return 'B 클래스'

# TypeError: Can't instantiate abstract class A with abstract method display
# 추상 클래스는 인스턴스를 생성할 수 없음
#a = A()

# TypeError: Can't instantiate abstract class B with abstract method display
b = B()
print(b.display())
'''
# < 확인 학습 > : 추상 클래스
# 문제) 아래에서 제시하는 조건에 맞게 클래스를 작성하고, 인스턴스를 만들어 다형성을 형성하여 확인하시오.
# 추상 클래스: Animal, 멤버변수: name, 추상 메소드: bark, 출력 메소드
# Animal의 자식 클래스: Dog, Cat
# Dog 클래스: 멤버변수: type(견종)
# Cat 클래스: 멤버변수: age(나이)

''' 클래스 생성, 상속 '''
from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return '이름: {}'.format(self.name)
    @abstractmethod
    def bark(self):
        pass

class Dog(Animal):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type
    # 오버라이딩
    def __str__(self):
        return super().__str__() + ', 견종: {}'.format(self.type)
    # 오버라이딩
    def bark(self):
        return '멍멍~~~'
    
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    # 오버라이딩
    def __str__(self):
        return super().__str__() + ', 나이 : {}'.format(self.age)
    # 오버라이딩
    def bark(self):
        return '야옹~~~'

#a1 = Animal()
a2 = Dog('살구', '푸들')
a3 = Cat('도도', 3)

print(a2)
print(a3)
print('----------')

''' 다형성 '''
animals = [Dog('해피', '진돗개'), Cat('나비', 4), Dog('메리', '치와와'), Cat('벌이', 2)]
for a in animals:
    print(a)




