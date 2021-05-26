# 2021/01/20(수)

'''
< 파이썬에서 클래스 정의 방법 >
1. 클래스 안에 속성(변수)과 기능(메소드)을 정의한다.
2. 아무 내용이 없으면 pass라고 적어야 한다.
3. 파이썬의 최상위 부모 클래스 object 클래스이다.
4. 파이썬의 모든 멤버는 기본적으로 외부에서 접근가능하다.
5. 변수 앞에 __(언더바 2개)를 붙이면, 접근할때는 _클래스명__변수명으로 사용한다.
- name mangling(네임 맹글링)
6. 변수와 getter/setter를 활용한 property(프로퍼티)를 사용하여 캡슐화를 어느정도 구현한다.
7. __init__ 처럼 밑줄 2개가 붙은 특수한 메소드를 기본으로 가진다.

클래스 내부의 속성에 접근하는 내장함수
1. getattr : 멤버변수의 값을 읽는 함수
2. setattr : 멤버변수의 값을 설정하는 함수
3. delattr : 클래스의 멤버변수를 삭제하는 함수
4. hasattr : 클래스에서 멤버변수가 존재하는지 여부를 확인하는 함수

'''

'''
class  A:
    """테스트 클래스""" # 클래스의 정보

a = A()
print(a.__doc__)
'''

# 인스턴스 생성
# 1. __new()__  : __init__ 호출할 때 자동으로 호출되므로 만들어 사용하지는 않음.
# 2. __init()__ : 인스턴스 생성할 때 호출
# 3. __del()__ : 인스턴스가 소멸할 때 호출, 자동으로 호출되므로 만들어 사용하지는 않음.

# 예제1)
'''
class A:
    def __init__(self): # 생성자(constructor)
        self.value = 0
    def __del__(self):  # 소멸자(destructor)
        print('Destructor 호출')
    def get(self):
        return self.value
    def set(self, value):
        self.value = value
    
a = A() # __init__ 호출
print(a)
print(a.get())
a.set(7)
print(a.get())

del(a) # __del__ 호출 : 객체의 소멸을 위해 사용, 파이썬에서 자동 호출
print(a)
'''

# 클래스의 인스턴스를 생성하는 순서
# 1. __new__ 호출 : 클래스의 객체를 생성
# 2. __init__ 호출 : 생성된 객체에 값을 초기화

# 예제2)
'''
class A:
    # 메소드 오버라이딩
    def __new__(cls, value=0):
        print('cls={0}, value={1}'.format(cls, value))
        instance = object.__new__(cls)
        return instance
    # 메소드 오버라이딩
    def __init__(self, value=0):
        print('self={0}, value={1}'.format(self, value))
        self.value = value

a = A()
print(a)
print('----------')
b = A(10)
print(b)
'''

'''
# 예제3)
class A:
    """
    def __init__(self):
        self.x = x
        self.y = y
        print('__init__ 호출 : x={0}, y={1}'.format(self.x, self.y))
    """
    def __call__(self, x, y):
        self.x, self.y = x, y
        print('__call__ 호출 : x={0}, y={1}'.format(self.x, self.y))

# 인스턴스 생성
a = A()

# __call__ 사용하는 방법 : 인스턴스를 함수처럼 사용
a(10, 20)
print(a.x)
print(a.y)
'''


# 예제4)
class A:
    cv = 10 # 클래스 변수
    def __init__(self, iv=20):
        self.iv = iv # 인스턴스 변수

print(A.cv)
#print(A.iv) # 에러 - 인스턴스를 생성한 후 사용
a = A()
print(a.cv)
print(a.iv)

A.cv = 15
print(A.cv)
a.iv = 25
print(a.iv)
print('----------')
print(getattr(A, 'cv'))
print(getattr(a, 'iv'))
setattr(A, 'cv', 17)
print(A.cv)
setattr(a, 'iv', 27)
print(a.iv)
print('----------')
delattr(a, 'iv') # 인스턴스의 멤버변수를 삭제
#print(a.iv)
print(hasattr(a, 'iv'))
