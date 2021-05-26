# 2021/01/08(금)

'''
< 제어문 >
조건문 - if문
반복문 - while문, for문

< 파이썬의 문법 >
1. 조건문, 반복문, 함수, 클래스 뒤에 :으로 구분한다.
2. 단계별로 들여쓰기를 통해서 구분한다. 공백보다는 탭을 사용한다.
3. {}를 사용하지 않는다.

< 파이썬에서만 사용되는 문법 >
1. 수학처럼 사용하는 문법을 허용한다. (ex: -10 < n < 10)
2. 조건식 대신에 변수를 바로 사용할 수 있다. (숫자, 문자열, 리스트, 튜플, 딕셔너리)
3. 조건식으로 문자열 자체를 비교할 수 있다.
4. 조건부 표현식이 가능하다. 

'''

'''
< if문의 활용 >
# 1. if문 단독 사용 - 조건이 1개
print("양수를 입력하세요...")
n = int(input('양수 입력 : '))

if n > 0:
    print('{0}은 양수입니다.'.format(n))

# 2. if ~ else  - 조건이 2개
# 문제점 : 0을 음수로 판별
print("정수를 입력하세요...")
n = int(input('정수 입력 : '))

if n > 0:
    print('{0}은 양수입니다.'.format(n))
else:
    print('{0}은 음수입니다.'.format(n))


# 3. if ~ elif ~ else : 조건이 3개
print("정수를 입력하세요...")
n = int(input('정수 입력 : '))

if n > 0:
    print('{0}은 양수입니다.'.format(n))
elif n < 0:
    print('{0}은 음수입니다.'.format(n))
else:
    print('0입니다.')
    print('프로그램을 종료합니다.')
'''

# < 확인학습 > - 조건문
# 문제1) 정수를 입력받아서 짝수, 홀수를 판별하시오.
'''
print("정수를 입력하세요...")
n = int(input('정수 입력 : '))

if n%2 == 0:
    print('{0}은 짝수입니다.'.format(n))
else:
    print('{0}은 홀수입니다.'.format(n))
'''
# 문제2) 정수를 입력받아서 3의 배수이면서 4의 배수인지를 판별하시오.
'''
print("정수를 입력하세요...")
n = int(input('정수 입력 : '))

if n%3==0 and n%4==0:
    print('{0}은 3의 배수이면서 4의 배수입니다.'.format(n))
else:
    print('{0}은 3의 배수이면서 4의 배수가 아닙니다.'.format(n))
'''
    
# 문제3) 국어, 영어, 수학 점수를 입력받아서 총점, 평균, 학점을 출력하시오.
# 평균이 90점 이상이면 A, 80점 이상이면 B, 70점 이상이면 C, 60점 이상이면 D, 60점 미만이면 F
'''
print("국어, 영어, 수학 점수를 입력하세요...")
kor = int(input('국어 점수 입력 : '))
eng = int(input('영어 점수 입력 : '))
mat = int(input('수학 점수 입력 : '))

tot = kor + eng + mat
ave = tot / 3
grade = ''

if ave >= 90:
    grade = 'A'
elif ave >= 80:
    grade = 'B'
elif ave >= 70:
    grade = 'C'
elif ave >= 60:
    grade = 'D'
else:
    grade = 'F'

print('총점: {0}\n평균: {1:0.2f}\n학점: {2}'.format(tot, ave, grade))
'''

# 문제4) 정수를 입력받아서 한 자릿수, 두 자릿수, 세 자릿수 이상의 정수인지를 판별하시오.
'''
# 1번 방법
print("정수를 입력하세요...")
n = int(input('정수 입력 : '))

if n>-10 and n<10:
    print('{0}은 한자리수입니다.'.format(n))
elif n>-100 and n<100:
    print('{0}은 두자리수입니다.'.format(n))
else:
    print('{0}은 세자리수 이상입니다.'.format(n))
'''

# 2번 방법 - 수학처럼 변수를 가운데 두고 양쪽에 범위를 적는 문법을 허용
# 파이썬에서만 사용되는 문법
'''
print("정수를 입력하세요...")
n = int(input('정수 입력 : '))

if -10 < n < 10:
    print('{0}은 한자리수입니다.'.format(n))
elif -100 < n < 100:
    print('{0}은 두자리수입니다.'.format(n))
else:
    print('{0}은 세자리수 이상입니다.'.format(n))
'''

# 문제5) 월을 정수로 입력받아서 계절을 판별하시오.
# 3, 4, 5 - 봄
# 6, 7, 8 - 여름
# 9, 10, 11 - 가을
# 12, 1, 2 - 겨울

'''
# 1번 방법
print("월을 입력하세요...")
m = int(input('월 입력(1-12) : '))

if m>=3 and m<=5:
    print('{0}월은 봄입이다.'.format(m))
elif m>=6 and m<=8:
    print('{0}월은 여름입이다.'.format(m))
elif m>=9 and m<=11:
    print('{0}월은 가을입이다.'.format(m))
elif m==12 or m==1 or m==2:
    print('{0}월은 겨울입이다.'.format(m))
else:
    print('잘못 입력하였습니다.\n다시 시작해 주세요.')
'''

'''
# 2번 방법
print("월을 입력하세요...")
m = int(input('월 입력(1-12) : '))

if 3 <= m <= 5:
    print('{0}월은 봄입니다.'.format(m))
elif 6 <= m <= 8:
    print('{0}월은 여름입니다.'.format(m))
elif 9 <= m <= 11:
    print('{0}월은 가을입니다.'.format(m))
elif m==12 or m==1 or m==2:
    print('{0}월은 겨울입니다.'.format(m))
else:
    print('잘못 입력하였습니다.\n다시 시작해 주세요.')
'''

# if문에서 조건식 대신에 변수를 바로 사용할 수 있다.
# 숫자    - 0:False, 0이외의 모든 숫자:True
# 문자열  - "",빈 문자열:False, 내용이 있는 문자열:True
# 리스트, 튜플, 딕셔너리 - 빈상태,[],(),{}:False, 내용이 있는 경우:True
# None:False
'''
n = 3.14

if n:
    print('성공입니다.')
else:
    print('다음에 도전하세요.')
'''

# 문자열 자체를 비교할 수 있다. 아스키 코드로 변화해서 비교하기 때문.
'''
#a = 'korea'
#b = 'japan'
a = '한국'
b = '일본'

if a > b:
    print('사전에서 {0}이 {1}보다 뒤에 나옵니다.'.format(a, b))
'''

# 조건식으로 리스트, 튜플, 문자열을 사용할 수 있다. 연산자는 in 또는 not in을 사용.
'''
a = [1, 2, 3]
print(1 in a)
print(4 in a)

b = (1, 2, 3)
print(1 in b)
print(4 in b)

c = 'python'
print('t' in c)
print('x' in c)

print('택시 요금으로 지급할 방법을 입력하세요...')
pay = input('카드/현금/휴대폰 중에서 입력 : ')

pocket = ['카드', '현금', '휴대폰']

if pay in pocket and pay == '카드':
    print('택시를 타고 귀가하세요.')
else:
    print('걸어서 귀가하세요.')
'''

# 
# 평균 점수가 60점 이상이면 pass이고, 60점 미만이면 fail이라고 출력하시오.
print("국어, 영어, 수학 점수를 입력하세요...")
kor = int(input('국어 점수 입력 : '))
eng = int(input('영어 점수 입력 : '))
mat = int(input('수학 점수 입력 : '))

ave = (kor + eng + mat) / 3
#result = ''

'''
# 1번
if ave >= 60:
    result = 'pass'
else:
    result = 'fail'
'''

'''
# 2번
if ave >= 60: result = 'pass'
else: result = 'fail'
'''
# 3번 - 조건부 표현식 : 자바 언어의 삼항 연산자와 비슷
result = 'pass' if ave>=60 else 'fail'

print('당신의 평균점수는 {0:0.1f}으로 평가에 {1} 하였습니다.'.format(ave, result))

