# 2021/01/12(화)

'''
사용자 정의 함수(function)
- 함수 정의(선언), 함수 사용(호출)

'''

'''
# 함수를 만들고, 사용하는 기본적인 방법
# 함수 정의(선언)
# 매개변수(parameter)
# 반환값(return 값)
def add(a, b):
    return a + b;

# 함수 사용(호출)
# 인수(argument)
print('더하기:', add(10, 20))
'''

# 1. 매개변수가 없는 함수
def say():
    return 'hello'

print(say())

# 2. 반환값이 없는 함수
def add(a, b):
    print('{0} + {1} = {2}'.format(a, b, a+b))

add(10, 20)

# 3. 매개변수와 반환값이 모두 없는 함수
def say2():
    print('안녕하세요!')

say2()

# 4. 매개변수가 여러 개인 함수
def show(a, b, c):
    print('a={0}, b={1}, c={2}'.format(a, b, c))

# show(10) # 매개변수의 갯수가 일치하지 않음.
# show(10, 20)
# show(10, 20, 30, 40)
show(10, 20, 30)
# 매개변수를 지정하여 값을 전달
show(a=11, b=22, c=33)
show(c=33, a=11, b=22)
print('----------')

# 5. 매개변수가 몇 개이든지 상관없는 함수, 가변 인수를 가지는 함수
# 예제) 매개변수로 전달되는 모든 값의 합을 리턴하는 함수
# 매개변수 자리에 *a를 전달되는 값을 모두 모아서 튜플로 생성함
def add2(*a):
    print(type(a))
    tot = 0
    for i in a:
        tot += i
    return tot

print(add2(10))
print(add2(10, 20))
print(add2(10, 20, 30))
print('----------')

# 문제) 여러 개의 매개변수를 받아서 모두 더하거나, 곱하는 함수를 생성하시오.
def choice(ch, *a):
    if ch == '+':
        tot = 0
        for i in a:
            tot += i
    elif ch == '*':
        tot = 1
        for i in a:
            tot *= i;
    return tot

print(choice('+', 1, 2, 3, 4, 5))
print(choice('*', 1, 2, 3, 4, 5))
print('----------')

# 6. 키워드 파라미터
# **a는 딕셔너리 형태로 저장
def show2(**a):
    print(type(a))
    print(a)

show2(a=10)
show2(name='tom', age=50)
print('----------')

# 7. 리턴값은 한 개여야 한다.
# 리턴값이 여러 개일때는 결과를 한 개의 튜플로 생성한다.
def compute(a, b):
    return a+b, a*b;

result = compute(3, 4)
print(type(result))
print(result)

a, b = compute(3, 4)
print(type(a), type(b))
print(a); print(b)
print('----------')

'''
# a = 10; b = 20
a, b = 10, 20
print(type(a), type(b))
print(a, b)
'''

'''
def compute(a, b):
    return a+b, a-b, a*b, a/b;

result = compute(10, 3)
print(type(result))
print(result)
'''

# 첫번째 리턴문을 실행함, 에러가 발생하지는 않음.
def f1(a, b):
    return a+b
    return a*b

print(f1(3, 4))

# return만 사용하면, 아무 실행도 하지 않고 바로 리턴
def f2(a):
    if a == False:
        return
    print('성공입니다.')


f2(10)
f2(True)
f2(False) # 아무 것도 실행하지 않고, 바로 돌아옴.

# 8. pass 사용
# 아무 실행 내용이 없는 함수 생성
'''
int f3() { }
'''
def f3():
    pass

a = 90

if a >= 90:
    pass
else:
    print('시험에 다시 응시하세요.')

# 9. 디폴트값을 가지는 매개변수, 디폴트 매개변수
def show_info(name, age, gender=True):
    if gender == True:
        sex = '남성'
    else:
        sex = '여성'
    print('이름:{0}, 나이:{1}, 성별:{2}'.format(name, age, sex))

show_info('이익준', 41)
show_info('채송화', 40, False)

'''
# 에러 - 디폴트 매개변수는 맨 마지막에 사용해야 한다.
def show_info(name, gender=True, age):
    if gender == True:
        sex = '남성'
    else:
        sex = '여성'
    print('이름:{0}, 나이:{1}, 성별:{2}'.format(name, age, sex))

show_info('안정원', 38)
'''



