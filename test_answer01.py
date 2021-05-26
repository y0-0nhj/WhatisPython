# 2021/01/21(목)

# 1번 문제
'''
f = open('data.txt', 'r')
scores = f.readlines()
f.close()

print(scores)
print(type(scores))

print(scores[0])
print(type(scores[0]))

scores = scores[0].replace(' ','')
print(scores)
print(type(scores))

scores = scores.split(',')
print(scores)
print(type(scores))

result = []
for s in scores:
    result.append(int(s))

print(result)
print(type(result))

sum = sum(result)
ave = sum / len(result)
max = max(result)
min = min(result)

print(sum)
print(ave)
print(max)
print(min)
print('총점: {}, 평균: {:0.2f}, 최고점: {}, 최저점: {}'.format(sum, ave, max, min))

f = open('result.txt', 'w')
f.write('총점: {}, 평균: {:0.2f}, 최고점: {}, 최저점: {}'.format(sum, ave, max, min))
f.close()
'''

# 2번 문제
'''
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getarea(self):
        return math.pi * (self.radius ** 2)

    def getperimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return '반지름: {}, 면적: {:6.2f}, 둘레: {:6.2f}'.format(self.radius, self.getarea(), self.getperimeter())

#c1 = Circle(3.3)
#c2 = Circle(4.4)
#c3 = Circle(5.5)
#c4 = Circle(6.6)
#c5 = Circle(7.7)
circles = [Circle(3.3), Circle(4.4), Circle(5.5), Circle(6.6), Circle(7.7)]

for c in circles:
    print(c)
'''

# 3번 문제
class Member:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self):
        return '아이디: {}, 이름: {}, 나이: {}'.format(self.id, self.name, self.age)

class SpecialMember(Member):
    def __init__(self, id, name, age, privilege):
        super().__init__(id, name, age)
        self.privilege = privilege

    def __str__(self):
        return super().__str__() + ', 특별 혜택: {}'.format(self.privilege)

m1 = Member('aaa1111', '이익준', 42)
m2 = SpecialMember('bbb2222', '채송화', 38, '10% 할인')
m3 = Member('ccc3333', '안정원', 40)
m4 = SpecialMember('ddd4444', '장겨울', 30, '입장료 무료')

members = [m1, m2, m3, m4]
for m in members:
    print(m)


