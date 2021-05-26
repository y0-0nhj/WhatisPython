# 2021/01/25(월)

# 문제1) 구구단 출력
# 단을 입력받고, 구구단을 출력하는 함수를 만들어서 사용하시오.

# 함수 생성
'''
# 1. while문 사용
def gugudan(dan):
    i = 1
    while(i < 10):
        print('{} * {} = {:2d}'.format(dan, i, dan*i))
        i = i+1
'''
'''
# 2. for문 사용
def gugudan(dan):
    for i in range(1, 10):
        print('{} * {} = {:2d}'.format(dan, i, dan*i))

dan = int(input('구구단의 단을 입력하시오. '))
gugudan(dan)
'''

# 문제2) 리스트 중에서 3과 4의 공배수 구하기
# 제시하는 리스트의 값 중에서 3과 4의 공배수를 튜플로 저장하는 함수를 만들어 사용하시오.
'''
numbers = [20, 12, 22, 37, 36, 77, 80, 96, 88, 48, 72, 60, 120, 170, 180]

def calc(n):
    result = []
    for i in n:
        if i%3==0 and i%4==0:
            result.append(i)
    result = tuple(result)
    return result

print(calc(numbers))
'''

# 문제3) 문자열 다루기
'''
# 1. a:b:c:d 문자열을 a#b#c#d#으로 변경하기
s = 'a:b:c:d'
s = s.replace(':', '#')
print(s)
'''
'''
# 2. a:b:c:d 문자열을 a#b#c#d#으로 변경하기 (split(), join()함수 사용)
s = 'a:b:c:d'
a = s.split(':')
print(a)
b = '#'.join(a)
print(b)

# 3. 두 개의 리스트 합치기
a = [1, 2, 3]
b = [4, 5]
c = a + b # a와 b를 합쳐서 c를 생성, a는 변화 없음.
print(a)
a.extend(b) # a에다가 b를 합침, a는 변경됨.
print(a)
'''
# 4. 리스트의 총점, 평균 구하기
# 함수로 만들어서 사용하시오.
scores = [95, 80, 77, 85, 68, 70, 80, 78, 63, 50, 48, 78]
count = len(scores)

'''
# for문 사용
def calc(s):
    tot = 0
    for i in s:
        tot += i
    return tot
'''

# while문 사용
'''
def calc(s):
    tot = 0
    while s: # s의 데이터가 있는 동안
        tot += s.pop()
    return tot
        
result = calc(scores)
print('총점: {}, 평균: {:.2f}'.format(result, result/count))
'''

# 파일로부터 데이터 읽고, 저장하기
# 문제) 파일에는 5줄의 데이터가 있고, 1줄은 한 반의 데이터이고, 1줄에는 10명의 시험점수가 있다.
# 각 반의 시험 총점, 평균, 최고점, 최저점을 구하시오.
# 이 결과를 result.txt로 저장하시오.
# ex) 출력결과
#  반 | 총점 | 평균  | 최고점 | 최저점 |
# 1반 | 725  | 72.5 | 92     | 52    |
# .......
# 5반 | 785  | 78.5 | 95     | 48    |
'''
f = open('sample.txt', 'r')
lines = f.readlines()
f.close()

tot_s = [] # 각 반의 총점
max_s = [] # 각 반의 최고점
min_s = [] # 각 반의 최저점
cnt_s = [] # 각 반의 학생수
for line in lines:
    line = line.replace('\n', '')
    line = line.split(',')
    cnt_s.append(len(line)) 
    tot = 0
    mm = [] # 각 반의 학생점수
    for s in line:
        tot += int(s)
        mm.append(int(s))
    tot_s.append(tot)
    max_s.append(max(mm))
    min_s.append(min(mm))

print(tot_s)
print(max_s)
print(min_s)

f = open('result.txt', 'a')
f.write(' 반  | 총점  | 평균  | 최고점 | 최저점 |\n')
print(' 반  | 총점  | 평균  | 최고점 | 최저점 |\n')
for i in range(len(tot_s)):
    f.write('{:2d}반 | {:6d} | {:6.1f} | {:6d} | {:6d} |\n'.format(i+1, tot_s[i], tot_s[i]/cnt_s[i], max_s[i], min_s[i]))
    print('{:2d}반 | {:6d} | {:6.1f} | {:6d} | {:6d} |\n'.format(i+1, tot_s[i], tot_s[i]/cnt_s[i], max_s[i], min_s[i]))

f.close()
'''

# 클래스 다루기
# 문제5) 리스트의 값들의 합계와 평균을 구하는 함수를 갖는 클래스를 구현하고, 확인하시오.

class Computer:
    def __init__(self, nlist=[]):
        self.nlist = nlist

    def add(self):
        tot = 0
        for i in self.nlist:
            tot += i
        return tot

    def mean(self):
        ave = self.add() / len(self.nlist)
        return ave

a = Computer([10, 20, 30, 40, 50])
print(a.add())
print(a.mean())






















