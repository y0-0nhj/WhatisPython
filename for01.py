# 2021/01/11(월)

'''
for문 활용
1. for 제어변수 in range():
2. for 제어변수 in 리스트, 튜플, 문자열:
- 인덱스를 통해 자동으로 접근
'''

### 1. for 제어변수 in range():
# 1. for문과 range(n) -> n번 반복
# 예제) '공부만이 살길이다'를 10번 반복하시오. 
'''
for i in range(10):
    print('공부만이 살길이다.')
'''

# 2. for문과 range(1, 11) -> 1부터 1씩 증가하면서 10까지 반복
'''
for i in range(1, 11):
    print(i)
'''

# 3. for문과 range(1, 11, 2) -> 1부터 2씩 증가하면서 10까지 반복
'''
for i in range(1, 11, 2):
    print(i)
'''

# < 확인학습 > - for문, range()
# 문제1) 정수를 입력받아서, 1부터 입력받는 수까지 중에서 짝수를 출력하고, 짝수의 합을 출력하시오.
'''
n = int(input('정수 입력 : '))
tot = 0
for i in range(1, n+1):
    if i%2 == 0:
        print(i)
        tot += i
print('1부터 {0}까지의 짝수의 합계 : {1}'.format(n, tot))
'''

# 문제2) 정수를 입력받아서, 1부터 입력받은 수까지 중에서 3의 배수이면서 4의 배수를 출력하고, 그 갯수와 합을 출력하시오.
'''
count = 0; tot = 0
n = int(input('정수 입력 : '))
for i in range(1, n+1):
    if i%3==0 and i%4==0:
        print(i)
        count += 1
        tot += i

print('1부터 {0}까지 3의 배수이면서 4의 배수의 갯수 : {1}'.format(n, count))
print('1부터 {0}까지 3의 배수이면서 4의 배수의 합계 : {1}'.format(n, tot))
'''

# 문제3) 2단부터 9단까지 구구단을 출력하시오.
'''
for i in range(2, 10):
    print('--- {0}단 ---'.format(i))
    for j in range(1, 10):
        print('{0} * {1} = {2}'.format(i, j, i*j))
    print()
'''
# 과제) 구구단을 가로로 출력하시오.

### 2. for 제어변수 in 리스트, 튜플, 문자열:
# 예제) 리스트의 학생 점수를 출력하고, 합계와 평균을 구하시오.
'''
score = [67, 85, 77, 72, 83, 55, 97]
tot = 0
i = 1
for s in score:
    print('{0}번 학생 점수 : {1}'.format(i, s))
    tot += s
    i += 1
ave = tot / len(score)

print('총점 : {0}\n평균 : {1:0.2f}'.format(tot, ave))
'''

# < 확인학습 > for문, 리스트, 튜플, 문자열
# 문제1) 리스트의 학생 점수에 대한 합격, 불합격 여부를 출력하시오.
# 점수가 60점 이상이면 합격, 60점 미만이면 불합격을 출력하시오.
'''
score = [67, 85, 52, 72, 83, 55, 97, 44, 38]
i = 1
for s in score:
    if s >= 60:
        print('{0}번 학생 성적: {1}, 결과: {2}'.format(i, s, '합격'))
    else:
        print('{0}번 학생 성적: {1}, 결과: {2}'.format(i, s, '불합격'))
    i += 1
'''

# 문제2) 회원 이름을 첫글자를 대문자로 바꾸어 저장하시오.
member = ['tom', 'mary', 'scott', 'jenny', 'rose', 'lisa', 'king']
'''
# 1번 방법
member2 = []
for m in member:
    # m = m.capitalize()
    member2.append(m.capitalize())
print(member2)
'''


# 2번 방법
'''
i = 0
for m in member:
    member[m] = m.capitalize()
    i += 1
print(member)
'''

# 문제3) 리스트의 숫자 중에서 소수만 출력하시오.
# 소수 : 1과 자신으로만 나누어지는 수
'''
num = [55, 12, 7, 6, 23, 34, 73, 87, 81, 92]

for i in num:
    for j in range(2, i+1):
        if i == j: print(i)
        if i%j == 0: break
'''    

# 문제4) 리스트의 요소 중에서 숫자를 판별하여 합계를 구하시오.
'''
a = ['87', 'tom', '85', '65', 'mary', '72', '92', '86', '67', '75']
tot = 0
for i in a:
    if i.isnumeric():
        tot += int(i)
        print(i)

print('합계: {0}'.format(tot))
'''

# 문제5) 정수를 포함한 문자열을 입력하여 정수의 합계를 구하시오.

str = input('정수를 포함한 문자열 입력 : ')
tot = 0

for s in str:
    if s.isnumeric():
        tot += int(s)

print('합계 : {0}'.format(tot))



















































































