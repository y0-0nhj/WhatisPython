# 2021/01/14(목)

'''
기타 내장 함수
'''

# 8. filter()
# - filter(함수, 반복가능한 데이터)
# - 함수와 반복가능한 데이터(리스트)를 받아서, 함수에서 참인 값을 묶어 반환하는 함수
# 예제) 데이터를 받아서 양수만 리스트로 저장하는 함수를 생성하시오.
'''
# 1번 방법 - 사용자 정의 함수
def choose(x):
    result = []
    for i in x:
        if i > 0:
            result.append(i)
    return result

s = [10, -10, -5, 0, 35, 77, -33, 87, 99, -55]
a = choose(s)
print(a)
'''
'''
# 2번 방법 - filter 함수
def choose(x):
    return x > 0;

s = [10, -10, -5, 0, 35, 77, -33, 87, 99, -55]
a = list(filter(choose, s))
print(a)
'''

# 3번 방법 - filter, lambda 함수 사용
# 람다(lambda) 함수 : 한 줄의 수식으로 구성된 인라인 함수
'''
s = [10, -10, -5, 0, 35, 77, -33, 87, 99, -55]
a = list(filter(lambda x : x>0, s))
print(a)
print('----------')
'''
# 람다 사용법
# lambda 인수 : 수식
'''
f1 = lambda x : x*x
print(f1(2))
print(f1(3))
print('----------')

f2 = lambda x,y : x+y
print(f2(10, 20))
print('----------')

f3 = lambda x=1,y=1 : x+y # x, y값은 디폴트 매개변수
print(f3(30, 40))
print(f3(10))
print(f3())
'''

# < lambda, filter, 기타 내장 함수 확인 학습 >
score = (95, 84, 75, 63, 55, 72, 48, 92, 30, 82)

# 문제1) score 중에서 60점 이상인 점수만 result이라는 튜플로 만들어 확인하시오.
'''
# 1번 방법
def s60(x):
    y = []
    for s in x:
        if s >= 60:
            y.append(s)
    return y

result = tuple(s60(score))
print(result)
'''

'''
# 2번 방법 - filter() 함수 사용
def s60(x):
    return x >= 60

result = tuple(filter(s60, score))
print(result)
'''

'''
# 3번 방법 - lambda 함수 사용
result = tuple(filter(lambda x:x>=60, score))
print(result)

# 문제2) score의 총점을 구하시오.
# sum() 함수
print('합계 : ', sum(score))

# 문제3) score의 평균을 구하시오.
print('평균 : ', sum(score)/len(score))

# 문제4) score 중에서 최고점을 구하시오.
print('최고점 : ', max(score))

# 문제5) score 중에서 최저점을 구하시오.
print('최저점 : ', min(score))
print('----------')
'''

#####
# 9. map()
# - map(함수, 반복가능한 데이터)
# - 함수와 반복가능한 데이터를 받아서, 함수에서 수행한 결과를 반환하는 함수

# 문제) 리스트의 각각의 값에 2를 곱한 값의 리스트 생성하여 확인하시오.
a = [10, 20, 30, 40, 50]

'''
# 1번 방법
def fdouble(x):
    result = []
    for i in x:
        result.append(i*2)
    return result

s = fdouble(a)
print(s)
'''
'''
# 2번 방법 - map() 사용
def fdouble(x):
    return x * 2

s = list(map(fdouble, a))
print(s)

# 3번 방법 - map, lambda 함수 사용
s = list(map(lambda x:x*2, a))
print(s)
'''

# < lambda, map 함수 확인 학습 >
# 문제1) 직원들의 급여를 10%씩 인상해서 지급하려고 합니다.
# 인상된 급여의 튜플을 salary2로 생성하여 확인하시오.
salary = [250, 300, 350, 270, 330]

'''
# 1번 방법
def fsalary(x):
    result = []
    for s in x:
        result.append(int(s+s*0.1))
    return result

salary2 = tuple(fsalary(salary))
print(salary2)
'''

'''
# 2번 방법 - map() 함수 사용
def fsalary(x):
    return int(x+x*0.1)

salary2 = tuple(map(fsalary, salary))
print(salary2)
'''

'''
# 3번 방법 - lambda, map 함수 사용
salary2 = tuple(map(lambda x:int(x+x*0.1), salary))
print(salary2)
'''

#####
# 10. zip() 함수
# - 동일한 갯수의 데이터의 쌍을 튜플로 만들어 주는 함수
# - 갯수가 다르면 작은 갯수의 쌍을 튜플로 만듦

'''
# 문제1) 중간점수와 기말점수의 쌍을 튜플로 만들어 리스트로 생성하시오.
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
c = list(zip(a, b))
print(c)

midterm = [85, 75, 80, 65, 95]
finalterm = [77, 82, 93, 68, 88]
totalterm = list(zip(midterm, finalterm))
print(totalterm)

tot = [] # 중간점수 + 기말점수
for i in totalterm:
    s = i[0] + i[1]
    tot.append(s)

print('총점 : ', tot)
print('----------')

# 문제2) 각 요일의 점수 메뉴를 튜플로 만들어, 리스트를 생성하시오.
week = ['월', '화', '수', '목', '금']
lunch = ['된장찌게', '파스타', '라면+공기밥', '김밥', '김치찌게']

menu = list(zip(week, lunch))
print(menu)
print('----------')

for m in menu:
    print(m)
'''

#####
# 11. isinstance(인스턴스, 클래스)
# - 인스턴스가 해당 클래스의 인스턴스인지의 여부를 판단하는 함수
'''
class Person: pass # 클래스 정의

a = Person() # 인스턴스 생성
b = 3

"""
# 자바
class Person { }
Person a = new Person();
"""

print(type(a))
print(type(b))

print(isinstance(a, Person)) # True
print(isinstance(b, Person)) # False
print(isinstance(b, int))    # True
print('----------')

# is 연산자 : 두 개의 데이터가 같은 객체인지의 여부를 판단하는 함수
c = a         # 참조가 같음.
d = Person()  # 인스터스 새로 만듦, 참조가 다름.
print(a is c) # True
print(a is d) # False
print('----------')
print(id(a))  # 1255935889472
print(id(c))  # 1255935889472
print(id(d))  # 1255936586704
'''

#####
# 리스트 컴프리헨션(List Comprehension)
# - 리스트의 값 중에서 조건을 만족하는 값만 추출하여 리스트를 생성하는 방법 
# [수식 for 변수 in 리스트 if 조건]
# list(수식 for 변수 in 리스트 if 조건)
# tuple(수식 for 변수 in 리스트 if 조건)
# set(수식 for 변수 in 리스트 if 조건)

# 문제1) 1부터 100까지의 정수 중에서 3의 배수이고 4의 배수인 정수를 리스트로 생성하여 확인하시오.
'''
# 1번 방법
a = []
for i in range(1, 101):
    if i%3==0 and i%4==0:
        a.append(i)

print(a)

# 2번 방법 - 리스트 컴프리헨션
#a = [i for i in range(1, 101) if i%3==0 and i%4==0]
a = list(i for i in range(1, 101) if i%3==0 and i%4==0)
print(a)
'''

# 문제2) score 리스트에서 60점 이상의 점수만 추출하여 scorepass라는 리스트로 생성하여 확인하시오.
score = [75, 82, 55, 45, 68, 87, 93, 52, 72, 38]


# 1번 방법
scorepass = list()
for i in score:
    if i >= 60:
        scorepass.append(i)

print(scorepass)

# 2번 방법 - 리스트 
scorepass = list(i for i in score if i>=60)
print(scorepass)




