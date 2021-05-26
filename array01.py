# 2021/01/21(목)

'''
array 모듈
- 배열 모듈
- 리스트는 사용은 편리하지만, 속도와 공간적인 측면에서 효율은 떨어진다.
- array 모듈은 이러한 리스트의 단점을 보완하여 속도와 공간적인 측면에서 효율을 높여준다.

array(타입코드, [초기값])
- 타입코드
i, I - int
l, L - long
f - float
d - double
b, B - char
'''

from array import *

# array 생성
x = [95, 88, 75, 68, 56]
a = array('i', x)

# 출력
print(a)
for i in a:
    print(i)

# 추가
a.append(90)
print(a)

# 삭제
#del(a[4])
del a[4]
print(a)

# 수정
a[2] = 77
print(a)

