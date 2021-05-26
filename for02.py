# 2021/01/12(화)

'''
for문의 응용
1. iter(), next()
2. enumerate() 
'''
a = [10, 20, 30, 40, 50]
it = iter(a)
'''
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
'''

'''
# 1번 방법
for i in a:
    print(i)
print('----------')

# 2번 방법 - iter(), next() 함수 활용
for i in range(len(a)):
    print(next(it))
print('----------')

# 3번 방법 - enumerate() 함수 활용
# 인덱스와 값을 각각 출력
for item in enumerate(a):
    print(item)
print('----------')

for i, value in enumerate(a):
    print(i, value)
print('----------')

for i, value in enumerate(a, 100):
    print(i, value)
print('----------')
'''

# 문제) 리스트의 학생 점수에 대한 합격, 불합격 여부를 출력하시오.
# 점수가 60점 이상이면 합격, 60점 미만이면 불합격을 출력하시오.

score = [67, 85, 52, 72, 83, 55, 97, 44, 38]
'''
# 1번 방법
i = 1
for s in score:
    if s >= 60:
        print('{0}번 학생 성적: {1}, 결과: {2}'.format(i, s, '합격'))
    else:
        print('{0}번 학생 성적: {1}, 결과: {2}'.format(i, s, '불합격'))
    i += 1
'''
'''
# 2번 방법
for i in range(len(score)):
    if score[i] >= 60:
        print('{0}번 학생 성적: {1}, 결과: {2}'.format(i, score[i], '합격'))
    else:
        print('{0}번 학생 성적: {1}, 결과: {2}'.format(i, score[i], '불합격'))

'''
'''
# 3번 방법 - enumerate() 함수
for i, value in enumerate(score):
    if value >= 60:
        print('{0}번 학생 성적 : {1}, 결과: {2}'.format(i+1, value, '합격'))
    else:
        print('{0}번 학생 성적 : {1}, 결과: {2}'.format(i+1, value, '불합격'))

'''

#####
# set의 활용
s = {'이익준', '김준완', '채송화', '양석형', '안정원'}

'''
print(s)
print(type(s))
print(len(s))
print('----------')

s.add('도재학')
print(s)
s.remove('김준완')
print(s)
s.add('채송화')
print(s)
'''

# dictionary의 활용 - for문 활용
# dictionary CRUD
d = {'이익준':95, '김준완':82, '채송화':93, '양석형':74, '안정원':66}
# print(type(d)); print(len(d)); print(d)

# 추가 - C(create), 중복되지 않은 데이터
d['장겨울'] = 80

# 추가 - 중복된 데이터(키의 중복), 나중에 넣은 데이터로 대체
d['채송화'] = 70

# 삭제 - D(delete)
del(d['김준완']) 

# 수정 - U(update)
# 문제1) 양석형의 점수에 10점을 더하여 저장하시오.
# i: 키
for i in d:
    if i == '양석형':
        d[i] = d[i]+10

print(d)

# 검색 - R(read)
for k in d: # d는 d.keys()와 같음
    print('{0} : {1}'.format(k, d[k]))
print('----------')

# 리스트와 튜플의 활용 - for문 사용
a = [(1, 2), (3, 4), (5, 6)]

print(len(a))    
print(type(a))
print(a)

for (first, last) in a:
    print('{0} + {1} = {2}'.format(first, last, first+last))
print('----------')

b = [(1,2,3), (4,5,6), (7,8,9)]
for (first, second, third) in b:
    print('{0}, {1}, {2}'.format(first, second, third))


#####
# < 확인학습 - 반복문 >
# while문, for문

# 문제1) 구구단 옆으로 출력

# 문제2) 정수를 입력받아서 '*'를 사용하여 정사각형 출력

# 문제3) 정수를 입력받아서 '*'를 사용하여 직각삼각형 출력
# 좌하변이 직각인 직각삼각형
# 좌상변이 직각인 직각삼각형
# 우하변이 직각인 직각삼각형
# 우상변이 직각인 직각삼각형

# 문제4) 정수를 입력받아서 '*'를 사용하여 정삼각형 출력




