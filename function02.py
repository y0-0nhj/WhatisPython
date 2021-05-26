# 2021/01/13(수)

'''
1. 사용자 정의 함수
2. 지역변수와 전역변수
- 지역변수(local variable) : 함수 내부에서 선언되고, 함수 내부에서 사용되는 변수
- 전역변수(global variable) : 함수 외부에서 선언되고, 프로그램 전체에서 사용되는 변수
3. 함수의 장점
- 반복을 최소화
- 수정이 용이, 유지보수가 용이
- 재사용이 편리
- 세부적인 내용은 함수에 숨기고, 작업할 때의 논리에만 집중하게 함
4. 내장 함수
- type(), len(), id(), int(), float(), bin() ...

'''

# 문제) 학생이름, 성적(학생마다 수강하는 과목의 갯수는 다름), 평균을 계산(평균의 계산 여부를 지정)할 수 있는 함수를 생성하고 확인하시오.
# 함수 이름: calcscore, 매개변수 이름: name, score, ave
# 가변인수 매개변수 : 튜플 형태로 저장
# 키워드 매개변수 : 딕셔너리 형태로 저장

'''
def calcscore(name, *score, **ave):
    tot = 0
    for s in score:
        tot += s
    if ave['choice'] == True:
        print('학생이름: {0}, 총점: {1}, 평균: {2:0.2f}'.format(name, tot, tot/len(score)))
    else:
        print('학생이름: {0}, 총점: {1}'.format(name, tot))

calcscore('이익준', 95, 83, 75, choice=True)
calcscore('김준완', 88, 86, choice=False)
'''

'''
# 1. 지역변수의 사용 - 함수 내부에서만 사용 가
def show():
    name = '이익준'
    print('내 이름은 ', name, '입니다.')

show()
print(name) # 에러 - 함수 외부에서는 함수 내부에 지역변수 접근 불가
'''

'''
# 2. 전역변수의 활용 - 위치에 상관없이 사용 가능
name = '이익준'
def show():
    print('내 이름은 ', name, '입니다.')

show()
print(name) 
'''

'''
# 3. 지역변수와 전역변수
# - 지역변수와 전역변수가 같은 이름일 때, 지역변수를 우선적으로 적용

ratio = 0.1 # 전역변수

def sale1(price):
    print('할인율: {0}%, 정가: {1}원, 판매가: {2}원'.format(ratio*100, price, price-price*ratio))

def sale2(price):
    ratio = 0.2 # 지역변수
    print(id(ratio)) # 지역변수의 id
    print('할인율: {0}%, 정가: {1}원, 판매가: {2}원'.format(ratio*100, price, price-price*ratio))

sale1(10000)
sale2(10000)
print(ratio) # 전역변수
print(id(ratio)) # 전역변수의 id
'''

'''
# 4. 지역변수와 전역변수의 활용
ratio = 0.1 # 전역변수

def sale(price):
    global ratio # 전역변수를 사용함.
    ratio = 0.2  # 전역변수의 값을 변경함.
    print(id(ratio))
    print('할인율: {0}%, 정가: {1}원, 판매가: {2}원'.format(ratio*100, price, price-price*ratio))


sale(10000)
print(ratio) # 0.2
print(id(ratio))
'''

'''
# docstring : 함수 내부에 주석을 넣어서 함수의 설명, 사용법을 작성하는 것
def sale(price):
    """할인율을 적용한 상품의 판매가를 출력하는 함수"""
    ratio = 0.2  
    print('할인율: {0}%, 정가: {1}원, 판매가: {2}원'.format(ratio*100, price, price-price*ratio))

sale(10000)
#help(print)
#help(sale) # 함수 이름과 설명 및 사용법
print(sale.__doc__) # 함수 설명만 출력
'''

