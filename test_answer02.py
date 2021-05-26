# 2021/01/29(금)

# 1번 문제
'''
names = 'smith/allen/ward/jones/martin/blake/clark/scott/king/turner,adams,james,ford,miller'
names = names.replace(',', '/')
print(names)

members = names.split('/')
print(members)

members.sort()
print(members)
'''

# 2번 문제
'''
scores = [95, 88, 58, 65, 40, 82, 75, 54, 66, 62]

# 방법1
i = 1
for s in scores:
    if s >= 60:
        print('{}번 학생 점수 : {} -> 합격'.format(i, s))
    else:
        print('{}번 학생 점수 : {} -> 불합격'.format(i, s))
    i += 1
print('----------')

# 방법2
for i in range(len(scores)):
    if scores[i] >= 60:
        print('{}번 학생 점수 : {} -> 합격'.format(i+1, scores[i]))
    else:
        print('{}번 학생 점수 : {} -> 불합격'.format(i+1, scores[i]))
print('----------')

# 방법3
for i, s in enumerate(scores):
    if s >= 60:
        print('{}번 학생 점수 : {} -> 합격'.format(i+1, s))
    else:
        print('{}번 학생 점수 : {} -> 불합격'.format(i+1, s))
'''

# 3번 문제
'''
n = int(input('학생수 입력 : '))
scores = []
for i in range(n):
    s = int(input('{}번째 학생점수 : '.format(i+1)))
    scores.append(s)

#print(scores)
sum = sum(scores)
ave = sum / len(scores)
max = max(scores)
min = min(scores)
print('총점: {}, 평균: {:0.2f}, 최고점: {}, 최저점: {}'.format(sum, ave, max, min))
'''

# 4번 문제
'''
import math
def calc(r, choice='area'):
    if choice == 'area':
        print('반지름: {}, 원의 면적: {:0.2f}'.format(r, math.pi*(r**2)))
    elif choice == 'peri':
        print('반지름: {}, 원의 둘레: {:0.2f}'.format(r, 2*math.pi*r))

radius = float(input('반지름 입력: '))
calc(radius)
calc(radius, 'peri')
'''

'''
# 딕셔너리(dictionary)
# key와 value의 쌍을 하나의 데이터로 가지는 구조
menu = {'짜장면':5000} 
print(menu)

# 추가 - C
menu['짬뽕'] = 6000
menu['볶음밥'] = 6000
menu['야끼우동'] = 9000
menu['탕수육'] = 15000

print(menu.keys())   # 키 확인
print(menu.values()) # 값 확인
print(menu.items())  # 키와 값을 모두 확인

# 출력, 검색, 조회 - R
# 키를 값을 꺼내서 출력
for k in menu.keys():
    v = menu[k]
    #v = menu.get(k)
    print('{}:{}'.format(k, v))
print('----------')

# 수정 - U
# 딕셔너리는 키의 중복을 허용하지 않음을 활용
menu['짬뽕'] = 6500

# 삭제 - D
# 딕셔너리의 키를 삭제하면됨.
del menu['탕수육']

# 모두 삭제
menu.clear()
print(menu)
'''

# 5번 문제
names = ['smith', 'allen', 'ward', 'jones', 'martin', 'blake', 'clark', 'scott',
         'king', 'turner', 'adams', 'james', 'ford', 'miller']
scores = [95, 88, 58, 65, 40, 82, 75, 54, 66, 62, 35, 80, 90, 85]

students = {}
s_pass = {}
s_fail = {}

#students[names[0]] = scores[0]
for s in range(len(names)):
    students[names[s]] = scores[s] 
#print(students)

for s in students.keys():
    if students[s] >= 60:
        s_pass[s] = students[s]
    else:
        s_fail[s] = students[s]

#print(s_pass)
#print(s_fail)

print('- 합격자 명단 -')
for s in s_pass:
    print('{} : {}'.format(s, s_pass[s]))
print('- 탈락자 명단 -')
for s in s_fail:
    print('{} : {}'.format(s, s_fail[s]))



