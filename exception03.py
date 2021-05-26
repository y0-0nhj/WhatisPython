# 2021/01/28(목)

# 문제) 찾는 단어가 없을 때의 처리를 예외처리 사용해 보시오.
dic = {'boy':'소년', 'school':'학교', 'book':'책'} 

'''
try:
    #print(dic['boy'])
    print(dic['girl'])
except KeyError as e:
    print(e,'단어는 사전에 없습니다.')
    #print('찾으시는 단어는 없습니다.')
'''

'''
try:
    while True:
        word = input('찾는 단어를 입력하시오. ')
        print(dic[word])
except KeyError as e:
    print(e, '단어는 사전에 없습니다.')
'''

'''
# 1번 - 예외 처리 클래스
class MyError(Exception):
    pass

# 별명을 출력하는 함수
def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print('당신의 별명은 {}입니다.'.format(nick))

try:
    say_nick('천사')
    say_nick('바보')
except MyError:
    print('허용되지 않는 별명입니다.')
'''

'''
# 2번 - 예외 처리 클래스
class MyError(Exception):
    def __str__(self):
        return '허용되지 않는 별명입니다.'

# 별명을 출력하는 함수
def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print('당신의 별명은 {}입니다.'.format(nick))


try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print(e)
'''

# 패키지

# A.B - A: 패키지 이름, B: 모듈 이름
# game폴더/sound폴더/echo.py파일/echo_test()함수
# game폴더/sound폴더 - 패키지
# echo.py파일/echo_test()함수 - 모듈

'''
# 1번 방법
import game.sound.echo
game.sound.echo.echo_test()
'''

'''
# 2번 방법
import game.sound.echo as e
e.echo_test()
'''

'''
# 3번 방법
from game.sound.echo import echo_test
echo_test()
#say_test()
'''

'''
# 4번 방법
from game.sound.echo import echo_test, say_test
echo_test()
say_test()
'''

'''
# 5번 방법
from game.sound.echo import *
echo_test()
say_test()
'''

'''
# 에러 1
import game
game.sound.echo.echo_test()
'''

'''
# 에러 2
import game.sound
game.sound.echo.echo_test()
'''

'''
# 옳은 방법
import game.sound.echo
game.sound.echo.echo_test()
'''

'''
# 에러 3
import game.sound.echo.echo_test
game.sound.echo.echo_test()
'''

# 에러 4 - __init__.py 파일에 __all__ 변수에서 import할 모듈을 명시하지 않았기 때문
# 문제 해결) __init__.py 파일에 __all__ 에 import할 모듈을 명시하면 됨.
from game.sound import *
echo.echo_test()






























