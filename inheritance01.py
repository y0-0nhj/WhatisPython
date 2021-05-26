# 2021/01/21(목)

'''
상속 - 자식 클래스에서 부모 클래스의 변수와 함수를 물려받아서 사용하는 방법

'''

# 2차원 좌표 - x, y 좌표를 가지는 클래스
class Point2D:
    # 생성자
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # getter
    def getx(self):
        return self.x
    def gety(self):
        return self.y
    # setter
    def setx(self, x):
        self.x = x
    def sety(self, y):
        self.y = y
    # 출력 함수 - 자동으로 출력
    def __str__(self):
        return ('x={}, y={}'.format(self.x, self.y))
    # 출력 함수
    def showpoint(self):
        return ('x 좌표: {}, y 좌표: {}'.format(self.x, self.y))

# 3차원 좌표 - x, y, z 좌표를 가지는 클래스, Point2D로 부터 상속받는 클래스
# super() : 부모의 변수, 함수, 생성자에 접근하도록 하는 내장함수
# Overriding(오버라이딩) : 부모 클래스의 함수를 자식 클래스에서 완전히 일치하게 재정의 하는 것.
class Point3D(Point2D):
    # 생성자
    def __init__(self, x, y, z):
        #Point2D.__init__(self, x, y)
        super().__init__(x, y)
        self.z = z
    # getter
    def getz(self):
        return self.z
    # setter
    def setz(self, z):
        self.z = z
    # Overriding
    def __str__(self):
        return super().__str__() + (', z={}'.format(self.z))
        #return Point2D.__str__(self) + (', z={0}'.format(self.z))
    # Overriding
    def showpoint(self):
        return super().showpoint() + (', 좌표 z: {}'.format(self.z))

    
p1 = Point2D(10, 20)
print('x = %d' % p1.getx())
print('y = %d' % p1.gety())
print(p1)
print(p1.showpoint())
print('----------')

p2 = Point3D(30, 40, 50)
print(p2.getx())
print(p2.gety())
print(p2.getz())
print(p2)
print(p2.showpoint())


