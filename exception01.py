# 2021/01/27(수)

'''
에러(error), 오류 - 파이썬의 문법적인 오류
예외(exception) : 다양한 원인에 실행 주에 발생하는 비정상적인 문제

에러인 경우 : 반드시 수정해야 함.
예외인 경우 : 예외의 상황을 회피하고, 다음으로 진행되도록 해야함.
예외 처리(exception handling) : 예외의 문제를 해결하고, 다음 상황이 진행되도록 하는 것.

< 파이썬에서 예외를 처리하는 방법 >
try: 예외가 발생할 수 있는 구문
except 예외의 종류: 예외가 발생했을 때 처리 방법
'''

'''
# 에러 발생
a = 10
b = 'python'
c = a + b # 에러 - 정수와 문자열을 더할 수는 없음.
'''

# 예외 발생
'''
# 1. 예외처리를 하지 않은 경우
a = 10
b = 0
c = a / b # 예외 발생 - 모든 수는 0으로 나눌 수는 없음.

d = a + b # 실행되지 않음.
print(d)
'''

# 2. 예외처리를 한 경우
'''
# 1번 방법 - try: ~ except:
a = 10
b = 0
try: 
    c = a / b # 예외 - 모든 수는 0으로 나눌 수는 없음.
except:
    print('0으로 나눌수는 없습니다.')

d = a + b
print(d)
'''

'''
# 2번 방법 - try: ~ except 예외의 종류:
a = 10
b = 0
try: 
    c = a / b # 예외 - 모든 수는 0으로 나눌 수는 없음.
except ZeroDivisionError:
    print('0으로 나눌수는 없습니다.')

d = a + b
print(d)
'''
'''
# 3번 방법 - try: ~ except 예외의 종류 as 예외 메시지 변수:
a = 10
b = 0
try: 
    c = a / b # 예외 - 모든 수는 0으로 나눌 수는 없음.
except ZeroDivisionError as e: # 예외 메시지 변수
    print(e)

d = a + b
print(d)
'''

'''
# 4번 방법 - 발행하는 예외가 여러개 일 경우 1
# try: ~ except 예외의 종류: ~ except 예외의 종류 : ~
# except절에 들어가면, 다시 try절로 돌아가지 않고 끝나게 된다.
a = [10, 20, 30]

try:
    print(a[0] / 0)
    print(a[3])   
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)
    
print(a[1] + a[2])
'''

# 5번 방법 - 발행하는 예외가 여러개 일 경우 2
# try: ~ except 예외의 종류: ~ except 예외의 종류 : ~
# except절에 들어가면, 다시 try절로 돌아가지 않고 끝나게 된다.
a = [10, 20, 30]

try:
    print(a[0] / 0)
    print(a[3])   
except (ZeroDivisionError, IndexError) as e:
    print(e)
    
print(a[1] + a[2])

'''
# 6번 방법 - 예외가 발생되더라도 반드시 실행해야되는 문자이 있는 경우
# try: ~ except: ~ finally: ~
a = [10, 20, 30]

try:
    print(a[0] / 0)
    print(a[3])   
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)
finally:
    print(a[1] + a[2])

# 예외가 발생하지 않는다면: try: finally:
# 예외가 발생한다면: try: except: finally:
'''

