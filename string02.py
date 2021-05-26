# 2021/01/07(목)

'''
문자열 함수/메소드
'''

a = "python is good language!"

# len() : 문자열의 길이를 알려주는 내장함수
print(len(a))

# count() : 문자의 개수를 알려주는 메소드
print(a.count("g"))
print(a.count("n"))

# find() : 지정한 한 문자의 위치(인덱스) 알려주는 메소드
# 찾는 문자가 없을 때는 -1을 리턴
print(a.find("t"))
print(a.find("i"))
print(a.find("g")) # 여러 개가 있을 경우에는 첫번째 인덱스
print(a.find("is")) # 지정한 첫번째 문자의 인덱스를 리턴
print(a.find("x")) # 찾는 문자가 없을 때는 -1을 리턴

# index() : 지정한 한 문자의 위치(인덱스) 알려주는 메소드
# 찾는 문자가 없을 때는 에러를 발생
print(a.index("t"))
print(a.index("g"))
print(a.index("is"))
#print(a.index("x")) # error, 찾는 문자가 없을 때는 에러를 발생
print("----------")

# join() : 문자열을 삽입하는 메소드
a = "abcde"
b = ",".join(a)
print(a)
print(b)

a = "육치성"
b = "♥".join(a)
print(a)
print(b)

# upper() : 소문자를 대문자로 변경하는 메소드
a = "python"
a = a.upper()
print(a)

# lower() : 대문자를 소문자로 변경하는 메소드
b = "HELLO"
b = b.lower()
print(b)

# strip() : 양쪽 공백을 삭제하는 메소드
s = "     python     "
print(s, "확인")
s = s.strip()
print("%s확인" % s)

# rstrip() : 오른쪽 공백만 삭제하는 메소드
s = "     python     "
s = s.rstrip()
print("%s확인" % s)

# lstrip() : 왼쪽 공백만 삭제하는 메소드
s = "     python     "
s = s.lstrip()
print("%s확인" % s)

# replace() : 모든 문자열을 변경하는 메소드
s = "Time is Gold!"
s = s.replace("Gold", "Money")
print(s)

s = "자바는 프로그래밍 언어이다. 자바는 다양한 분야에서 활용된다."
s = s.replace("자바", "파이썬")
print(s)

# split() : 문자열을 구분자를 통해 나누어서 리스트 만드는 메소드
s = "python is good language"
print(s)
print(type(s))

s = s.split() # 공백으로 나눔, 디폴트값이 공백
#s = s.split(" ") # 공백으로 나눔.
print(s)
print(type(s))

s = "lion/leopard/hyena/cheetah/elephant/zeebra/hyppo/wildebeest"
s= s.split("/")
print(s)

'''
s = "lion/leopard/hyena/cheetah/elephant,zeebra,hyppo/wildebeest"
s= s.split("/")
s[4] = s[4].split(",")
print(s)
'''

s = '''
나에게는 꿈이 있습니다.
조지아의 붉은 언덕에서 
과거에 노예로 살았던 부모의 후손과
그 노예의 주인이 낳은 후손이 
식탁에 함께 둘러앉아 형제애를 나누는 날이 
언젠가 오리라는 꿈입니다.
나에게는 꿈이 있습니다.
삭막한 사막으로 뒤덮인 채 
불의와 억압의 열기에 신음하던 미시시피 주조차도 
자유와 정의가 실현되는 오아시스로 
탈바꿈 되리라는 꿈입니다.
나에게는 꿈이 있습니다.
나의 네 자식들이 피부색이 아니라 
인격에 따라 평가받는 나라에서 살게 되는 날이
언젠가 오리라는 꿈입니다.
지금 나에게는 꿈이 있습니다.
'''

# splitlines() : 긴 문자열에서 행별로 나누어서 리스트를 저장하는 메소드
print(s)
print(type(s))

s = s.splitlines()
print(s)
print(type(s))

# split()와 join()의 활용
# 문제) 날짜에서 "-"를 "/"로 바꾸어 저장하시오. ex) 2021/01/07
s1 = "2021-01-07"
s2 = s1.split("-")
s2 = "/".join(s2)
print(s1)
print(type(s1))
print(s2)
print(type(s2))

# startswith() : 첫문자가 특정 문자열로 시작하는지에 대한 여부를 나타내는 메소드
s = "Time is gold"
print(s.startswith("T"))
print(s.startswith("t"))

# endswith() : 끝문자가 특정 문자열로 끝나는지에 대한 여부를 나타내는 메소드
print(s.endswith("d"))
print(s.endswith("D"))
print("----------")

# in, not in 연산자 : 특정 문자열을 포함/미포함에 대한 여부 
print("gold" in s)
print("money" in s)
print("g" in s)
print("x" in s)
print("----------")
print("gold" not in s)
print("money" not in s)
print("g" not in s)
print("x" not in s)

# ljust() : 문자열을 왼쪽에 두고, 공백을 오른쪽에 삽입하는 메소드
# 숫자는 전체 자릿수
s = "python"
s = s.ljust(10);
print("%s확인" % s)

# rjust() : 문자열을 오른쪽에 두고, 공백을 왼쪽에 삽입하는 메소드
s = "python"
s = s.rjust(10)
print(s)

# center() : 문자열을 가운데에 두고, 왼쪽과 오른쪽에 균등하게 공백을 삽입하는 메소드
s = "python"
s = s.center(10)
print("%s확인" % s)

# 대소문자 변경 메소드
# lower() : 전체를 소문자로 변경
# upper() : 전체를 대문자로 변경
# swapcase() : 대문자는 소문자로, 소문자는 대문자로 변경
# title() : 모든 단어의 첫문자만 대문자로, 나머지는 소문자로 변경
# capitalize() : 문자열의 첫문자만 대문자로, 나머지는 소문자로 변경
s = "time is GOLD. Truth is diamond."
s1 = s.lower();
print(s1)
s2 = s.upper()
print(s2)
s3 = s.swapcase()
print(s3)
s4 = s.title()
print(s4)
s5 = s.capitalize()
print(s5)

# 문자 검색 메소드
# find()  : 왼쪽부터 찾은 문자의 인덱스를 출력
# rfind() : 오른쪽부터 찾은 문자의 인덱스를 출력
# index() : 왼쪽부터 찾은 문자의 인덱스를 출력
# rindex(): 오른쪽부터 찾은 문자의 인덱스를 출력
# 문자 찾지 못했을 때 find()는 -1을 리턴, index()는 에러를 발생시킴

s = "Time is gold, Truth is diamond."
print(s.find("i"))  # 1
print(s.index("i")) # 1
print(s.rfind("i")) # 24
print(s.rindex("i"))# 24
print(s.find("x"))  # -1
#print(s.index("x")) # error
print("----------")
print()

# 문자열의 속성의 여부를 판별하는 메소드
# isalpha() : 문자열의 모든 문자가 알파벳인지 여부
# islower() : 문자열의 모든 문자가 소문자인지 여부
# isupper() : 문자열의 모든 문자가 대문자인지 여부
# isnumeric(), isdigit(), isdecimal() : 문자열의 모든 문자가 숫자인지 여부
# isalnum() : 문자열의 모든 문자가 알파벳 또는 숫자인지 여부
# isspace() : 문자열의 모든 문자가 공백인지 여부

s1 = "python"
s2 = "PYTHON"
s3 = "10"
s4 = "3.14"
s5 = "     "

print(s1.isalpha())
print(s1.isnumeric())
print(s1.isupper())
print(s1.islower())
print("-----")
print(s2.isalpha())
print(s2.isupper())
print(s2.islower())
print("-----")
print(s3.isalpha())
print(s3.isnumeric())
print(s3.isdigit())
print(s3.isdecimal())
print(s3.isalnum())
print("-----")
print(s4.isalpha())
print(s4.isnumeric())
print(s4.isdigit())
print(s4.isdecimal())
print(s4.isalnum())
print("-----")
print(s5.isalpha())
print(s5.isspace())

