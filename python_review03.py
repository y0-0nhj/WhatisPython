# 2021/01/25(월)

# 문제) Computer.py 파일을 모듈로 사용하여 아래 리스트의 합계와 평균을 계산하시오.
a = [95, 85, 77, 68, 52, 85, 84, 82, 66, 78]

import Computer as c

com = c.Computer(a)
print('총점: {}, 평균: {:0.1f}'.format(com.add(), com.mean()))



































































