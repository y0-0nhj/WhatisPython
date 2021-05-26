# 2020/12/31(목)
# 데이터 타입 2

"""
< 테이터 타입의 종류 >
1. 숫자형 - 정수:int, 실수:float
2. 문자열형 - str, 쌍따옴표, 홀따옴표로 감싼 데이터
3. 논리형(불형, bool) - True, False
4. 리스트(list) - 
5. 튜플(tuple) -
6. 딕셔너리(dictionary) -
7. 집합(set) - 

-- escape code(이스케이프 코드)
\n : 줄바꿈 문자, 개행 문자
\t : 탭 간격
\\ : 문자로 \ 출력
\' : 문자로 ' 출력
\" : 문자로 " 출력
\a : 삑소리를 출력
\b : 백스페이스

-- 자료형에 대한 참과 거짓의 판별
숫자형 : 0이 아닌 숫자:True, 0:False
문자열 : "python":True, "":False
None : False
리스트 :
튜플 :
딕셔너리 : 

"""
s1 = "one\ntwo\tthree\\four\'five\"six\bseven"
print(s1)

s2 = "python" + " is fun!"    # 문자열 연결 1
print(s2)

s3 = "first" "second" "third" # 문자열 연결 2
print(s3)

s4 = ("one"                   # 문자열 연결 3
"two"
"three")
print(s4)

# ord() : 해당 문자에 대한 아스키 코드 확인하는 함수
print('a', "=", ord('a'))

# chr() : 해당 숫자에 대한 아스키 코드의 문자를 확인하는 함수
print(65, "=", chr(65))

s5 = "python" # "", '' 의 쌍은 맞아야 함
print(s5)

s6 = "python" * 2
print(s6)

print("-- 논리형 --")
a = True
b = False
print(type(a))
print(30 > 10)
print(30 < 10)
print(10 == 30)
print(10 != 30)

c = "python"
d = ""
e = 123
f = 0
# bool() : 자료의 참과 거짓을 판별하는 함수
print(type(c), ":", bool(c))
print(type(d), ":", bool(d))
print(type(e), ":", bool(e))
print(type(f), ":", bool(f))

'''
변수(Variable) - 데이터를 저장하는 메모리 공간

< 변수명을 만드는 방법 >
1. 알파벳, 숫자, _(언더바)를 사용
2. 첫문자는 숫자는 사용불가
3. 대소문자는 구분함
4. 예약어(키워드) 사용불가
-- 권장사항
5. 유니코드를 지원하므로 한글도 사용할 수는 있으나, 권장하지는 않음
6. 변수명은 의미있게 생성하는 권장 ex) a보다는 age로 만드는 것을 권장
7. 파이썬은 snake 표기법을 주로 사용 ex) max_score
'''
print("----------")
age = 30
print(age)
age = 45
print(age)
del age # 변수를 삭제하는 명령
#print(age)

'''
< 입출력 방법 >
출력 : print() 함수
- print(출력내용 [,sep=구분자] [,end=끝문자])
- ,문자롤 출력내용을 연결함.
입력 : input() 함수

'''
a = 2020
b = 12
c = 31
print(a, b, c)
print(a, "-", b, "-", c)
print(a, b, c, sep="-") # 출력할 때 연결하는 변수들의 구분자(seperator)

d = "python"
e = "is"
f = "fun"
print(d, e, f)

s1 = "서울"
s2 = "대전"
s3 = "대구"
s4 = "부산"
print(s1, s2, s3, s4, sep=" 찍고 ")
print(s1, s2, s3, s4, sep=" --> ")

s5 = "김혜연"
print(s1, s2, s3, s4, s5, sep=" 찍고 ", end=" --> ") # end 옵션 : 마지막 데이터 다음에 출력하는 문자
print()

'''
age = input("나이를 입력하세요 : ")
print("당신의 나이는 ", age + "살입니다")
'''

'''
a = input("정수 a 입력 : ") 
b = input("정수 b 입력 : ")
print("a + b = ", a+b)
print(type(a), " : ", type(b)) 

# int() : 문자열을 정수로 바꿔주는 함수
print("a + b = ", int(a)+int(b))
'''

price = int(input("과일 가격 입력 : "))
count = int(input("과일 갯수 입력 : "))
tot = price * count
print("총금액 : ", tot, "원")

ㄴ
