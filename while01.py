# 2021/01/11(월)

'''
반복문
1. while문
2. for문

'''

# 문제2) 아래의 조건에 따라 계산기 프로그램을 작성하시오.
# 정수 2개 입력 받고, 연산자를 1개 입력 받아서 계산하도록 작성하시오.
# 입력 화면
# x:10, y:3, op:* --> 계산 결과 : 10 * 3

'''
print('계산기 프로그램을 실행합니다.')
x = int(input('정수 x 입력 : '))
y = int(input('정수 y 입력 : '))
op = input('연산자 입력 : ')

if op == '+': 
    print('{0} {1} {2} = {3}'.format(x, op, y, x+y))
elif op == '-':
    print('{0} {1} {2} = {3}'.format(x, op, y, x-y))
elif op == '*':
    print('{0} {1} {2} = {3}'.format(x, op, y, x*y))
elif op == '/':
    print('{0} {1} {2} = {3:0.2f}'.format(x, op, y, x/y))
else:
    print('잘못된 연산입니다.')
'''

#####
# 문제) 1부터 10까지 1씩 증가하면서 출력하는 반복문
# 초깃값, 조건, 증감값
'''
i = 1          # 초깃값
while i <= 10: #조건
    print(i)
    i += 1     # 증감값
'''

# < 확인학습 > -while문
# 문제1) 정수를 입력받고, 1부터 입력받은 정수 중에서 짝수와 그 합을 출력하시오.
# while문과 if문의 활용

'''
n = int(input('정수 입력 : '))
i = 1
tot = 0

while i <= n:
    if i%2 == 0:
        print(i)
        tot += i
    i += 1

print('1부터 {0}까지의 짝수의 합계 : {1}'.format(n, tot))
'''

# 문제2) 정수를 입력받고, 1부터 입력받은 정수 중에서 3의 배수이면서 4의 배수인 수를 출력하고, 그 갯수와 합을 출력하시오.
# while문과 if문의 활용
'''
n = int(input('정수 입력 : '))
i = 1
tot = 0
count = 0

while i <= n:
    if i%3==0 and i%4==0:
        print(i)
        count += 1
        tot += i
    i += 1

print('1부터 {0}까지 3의 배수이면서 4의 배수의 갯수 : {1}'.format(n, count))
print('1부터 {0}까지 3의 배수이면서 4의 배수의 합계 : {1}'.format(n, tot)) 
'''

# 문제3) 구구단 2단부터 9단까지를 출력하시오.
# while문의 중첩

# 2단을 출력하는 반복문
'''
i = 1
while i <= 9:
    print('2 * {0} = {1}'.format(i, 2*i))
    i += 1
'''

'''
i = 2
while i <= 9:
    j = 1
    while j <= 9:
        print('{0} * {1} = {2}'.format(i, j, i*j))
        j += 1
    print()
    i += 1
'''

# 과제) 2단부터 9단까지를 옆으로 출력하시오.

# break문 : 반복문을 탈출
# 문제) 1부터 10까지 1씩 증가하면서 반복하는데, 5의 배수가 되면 반복을 멈추도록 하시오.
'''
i = 1
while i <= 10:
    if i%5 == 0:
        break
    print(i)
    i += 1
'''

# continue문 : 반복문의 끝으로 이동
# 문제) 1부터 100까지 1씩 증가하면 반복하는데, 5의 배수를 제외하고 출력하시오.
i = 0
while i < 100:
    i += 1
    if i%5 == 0:
        continue
    print(i)
    
