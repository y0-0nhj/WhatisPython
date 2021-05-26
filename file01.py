# 2021/0115(금)

'''
< 파일 입출력 >
'''
# 파일의 위치는 경로를 쓰면 해당 위치에 파일을 생성하고,
# 경로를 생략하고 파일이름만 쓰면, 파이썬 파일이 있는 곳에 파일을 생성함.
#f = open('c:/python_study/workspace_p/p20210115/file01.txt', 'w')

'''
# 쓰기 1번 - 덮어쓰기
f = open('file01.txt', 'w') # 쓰기, 덮어쓰기
for i in range(1, 11):
    f.write('%d번째 줄입니다.\n' % i)
f.close()

# 쓰기 2번 - 추가하기
f = open('file01.txt', 'a')  # 쓰기, 추가
for i in range(1, 11):
    f.write('추가: %d번째 줄입니다.\n' % i)
f.close()
'''

'''
# 읽기 1번 - readline() 함수 사용
# 한 줄 읽기
f = open('file01.txt', 'r')
line = f.readline() # 1줄 읽기
print(line)
f.close()

# 모든 줄 읽기
f = open('file01.txt', 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
'''

'''
# 1. 콘솔로부터 입력받은 내용을 콘솔에 출력
while 1:
    data = input('입력 : ')
    if not data: break
    print('출력 : %s' % data)
''' 

'''
# 2. 콘솔로부터 입력받은 내용을 파일에 저장
# 쓰기 모드로 파일 생성
f = open('file02.txt', 'w')
f.close()

# 쓰기 모드로 파일에 내용 추가
f = open('file02.txt', 'a')
while True:
    data = input('입력 : ')
    if not data: break
    f.write(data + '\n')
f.close()
'''

'''
# 읽기 2번 - 한번에 모든 내용 읽기, readlines() 함수 사용
f = open('file01.txt', 'r')
lines = f.readlines() # \n이 그대로 출력됨.
print(lines)
f.close()

f = open('file01.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
'''

'''
# 읽기 3번 - read() 함수 사용
# 파일의 전체 내용을 문자열로 만들어 반환한다.
f = open('file01.txt', 'r')
data = f.read()
print(data)
f.close()
'''

'''
# 쓰기 모드로 추가
f = open('file01.txt', 'a')
for i in range(11, 21):
    f.write('%d번째 줄입니다.\n' % i)
f.close()
'''

# with문을 파일 쓰기와 파일 읽기
# 장점 :  close()를 하지 않아도 with문을 벗어나면 자동으로 닫는다.

'''
# 문제점 - 닫지 않으면 내용이 저장되지 않음
f = open('foo.txt', 'w')
f.write('Life is too short, you need python')
f.close()
'''
# 개선책 - with문 사용
with open('foo02.txt', 'w') as f:
    f.write('Life is too short, you need python')

