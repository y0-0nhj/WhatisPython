# 2021/01/21(목)

# 모듈(module)
# - 변수, 함수, 클래스를 포함하고 있는 파일.
# - 다른 파일에서 이 모듈을 사용할 수 있음.

# module03.py

# 변수
PI = 3.141592

# 함수
def add(a, b):
    return a + b

# 클래스 - 반지름과 원주율을 가지고 원의 면적과 원의 둘레를 구하는 클래스
class Circle:
    def setarea(self, radius):
        return PI * (radius ** 2)

    def setperi(self, radius):
        return 2 * PI * radius

