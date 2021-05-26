# 2021/01/06(수)

'''
< 문자열을 다루는 방법 >
1. +(연결), *(반복) 연산자 사용
2. 인덱싱(indexing), 슬라이싱(slicing)
3. 포매팅(formmating)
4. 문자열 함수
'''

# 문자열 연결 (+ 연산자)
s1 = "Python"
s2 = " is fun!"
s3 = s1 + s2
print(s3)

# 문자열 반복 (* 연산자)
s4 = s1 * 3
print(s4)

# 문자열 반복 응용
print("=" * 30)
print("Python is good!")
print("=" * 30)

# 문자열의 길이를 구하는 함수 : len()
print(len(s1))

# 문자열의 인덱싱(indexing), 슬라이싱(slicing)
# - 리스트와 튜플에서도 똑같이 적용됨.
a = "Life is too short, You need Truth!";
print(a[8])
print(a[12:17])
print(a[0:17])
print(a[:17])   # 처음부터 17번 앞까지 인덱싱
print("--------------------")
print(a[19:34])
print(a[19:])   # 19번부터 끝까지 인덱싱
print("--------------------")
print(a[-6])    # 음수는 뒤에서부터 접근할때 사용
print(a[-6:-1]) # Truth
print(a[28:33]) # Truth
print(a[23:-7]) # need
print(a[23:27]) # need
print("-------------------")

# 슬라이싱 응용
# 문제1) 년, 월, 일, 요일, 날씨를 분리하여 저장하고 확인하시오.
s1 = "20210106수맑고영하의날씨"
year = s1[:4]
month = s1[4:6]
date = s1[6:8]
week = s1[8]
weather = s1[9:]
print(year)
print(month)
print(date)
print(week)
print(weather)
print("--------------------")

# 문제2) 아래의 문자열에서 bad를 good으로 변경하시오.
# 슬라이싱을 사용하시오.
s2 = "I got a bad friend!"
print(s2)
s2 = s2[:8] + "good" + s2[11:]
print(s2)
print("--------------------")

# 문자열 포매팅(fommatting)
# 포매팅에서 사용하는 형식문자
# %s:문자열, %d:정수(10진수), %f:실수, %c:문자
# %o:8진수, %x:16진수, %%:%기호

'''
name = input("이름 입력 : ")
age = input("나이 입력 : ")
print("당신의 이름은", name, "이고, 나이는", age, "입니다.")
print("당신의 이름은 %s이고, 나이는 %s입니다." % (name, age)) 
'''

'''
# 문제3) 국어, 영어, 수학 점수를 입력받아서, 총점과 평균을 계산하시오.
kor = int(input("국어 점수 입력 : "))
eng = int(input("영어 점수 입력 : "))
mat = int(input("수학 점수 입력 : "))

tot = kor + eng + mat
ave = tot / 3

print("총점: %d\n평균: %.2f" % (tot, ave))
'''

a = 12345
b = 3.141592
c = "python"

# 정수 출력
print("%d" % a)
print("%10d" % a)
print("%-10d확인" % a)

# 실수 출력
print("%f" % b)
print("%10.2f" % b)
print("%.2f" % b)
print("%0.2f" % b)

# 문자열 출력
print("%s" % c)
print("%10s" % c)
print("%-10s확인" % c)
print("--------------------")

# format() 함수를 사용한 포매팅
print("I eat %d apples." % 3)
print("I eat {0} apples".format(3))

print("I eat %s apples." % "three")
print("I eat {0} apples.".format("three"))

print("I eat %d apples, and I eat %s breads." % (3, "three"))
print("I eat {0} apples, and I eat {1} breads.".format(3, "three"))

name = "tom"
age = 50
print("%s의 나이는 %d살입니다." % (name, age))
# 숫자 포매팅 사용
print("{0}의 나이는 {1}살입니다.".format(name, age))
# 이름 포매팅 사용 - name=value 형식으로 사용
print("{name}의 나이는 {age}살입니다.".format(name="grace", age=33))
print("{name}의 나이는 {age}살입니다.".format(name=name, age=age))

# 숫자와 이름 포매팅을 함께 사용할 때의 방법
# - 주의 : 숫자를 맨 처음 한번만 사용하고, 그 이후로는 문자 포매팅을 해야 함.
#print("{name}의 나이는 {1}살입니다.".format(name="steve", 100)) # --> error
print("{0}의 나이는 {age}살입니다. {job}".format("steve", age=100, job="captain"))
print("--------------------")

# 포매팅 응용 - 자릿수, 정렬
a = 12345
b = 3.141592
c = "python"

# 정수 포매팅 - d를 생략 가능
print("{0}".format(a))
print("{0:10d}".format(a))
print("{0:<10d}확인".format(a))
print("-----")

# 실수 포매팅 - f를 사용해야 소숫점 자릿수가 정확하게 출력.
print("{0}".format(b))
print("{0:10f}".format(b))
print("{0:10.2f}".format(b))
print("{0:<10.2f}확인".format(b))
print("{0:>10.2f}확인".format(b))
print("{0:0.2f}".format(b))
print("{0:.2f}".format(b))
print("-----")

# 문자열 포매팅 - s를 생략 가능
print("{0}".format(c))
print("{0:10s}확인".format(c))
print("{0:>10s}확인".format(c))
print("-----")

# 정렬할 때의 공백을 특수문자로 채우는 방법
# ^(내용을 가운데로 배치)
# <(내용을 왼쪽으로 배치)
# >(내용을 오른쪽으로 배티)
print("{0:@^10}".format(c)) # @@python@@
print("{0:@<10}".format(c)) # python@@@@
print("{0:@>10}".format(c)) # @@@@python

# 포매팅할 때 내용을 원래 그대로 출력
# - {{}}, 중괄호를 두번 감싸서 사용함.
# print("{ and }".format()) --> error
print("{{ and }}".format()) # { and }
print("----------")

# f문자열 포매팅
# - 주의) 3.6 버전부터 사용됨. 3.6 버전 이전은 사용할 수 없음.
# - 함수가 f문자열 접두어를 사용함.
# - 변수를 바로 적용해서 사용함.
name = "tom"
age = 50
print("{0}의 나이는 {1}살입니다.".format(name, age))
print("{name}의 나이는 {age}살입니다.".format(name=name, age=age))
print("-----")
print(f"{name}의 나이는 {age}살입니다.")
print(f"{name}의 나이는 {age}살입니다. 내년에는 {age+1}살이 됩니다.")

# f문자열 포매팅 - 딕셔너리를 활용
d = {"name":"steve", "age":100}
print(f"{d['name']}의 나이는 {d['age']}살입니다.")

# f문자열 포매팅 - 정렬
a = 12345
b = 3.141592
c = "python"

print(f"{a}")
print(f"{a:10d}")
print(f"{a:<10d}확인")

print(f"{b}")
print(f"{b:10.2f}")
print(f"{b:<10.2f}확인")

print(f"{c}")
print(f"{c:10s}확인")
print(f"{c:>10s}확인")
print(f"{c:@>10s}확인")
print(f"{c:@<10s}확인")
print(f"{c:@^10s}확인")


