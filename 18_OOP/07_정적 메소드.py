# 정적 메소드(static method) : self를 통하지 않고 바로 클래스가 메소드 호출
# @staticmethod : 함수의 데코레이터 -> 정적 메소드로 정의한다는 것을 표시
class Cal:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        return a / b

print(Cal.add(10, 5))