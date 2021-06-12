# 인스턴스 변수와 클래스 변수
# class Car(object):   # object 생략 가능! 최상위 클래스
class Car:
    number = 0   # 클래스 변수 num : 클래스 안에서 모든 인수들이 공유하는 변수
    def __init__(self, speed=0, color='white'):
        self.color = color   # 클래스 내에서만 사용하는 비공개 필드
        self.speed = speed
        Car.number += 1   # 클래스 이름(Car)으로

    def __str__(self):
        return '이 자동차의 색상은 %s이고,\n속도는 %d입니다.' % (self.color, self.speed)

    # color 필드값 반환 메소드
    def getColor(self):
        return self.color

    # color 필드값 변경 메소드
    def setColor(self, color):
        self.color = color

    # 비공개 메소드
    def showInfo(self):
        print('속도는 %d입니다.' % self.speed)

    def drive(self):
        if self.speed != 0:
            print('%d(으)로 주행중입니다.' % self.speed)
        else:
            print('정차중입니다.')

    def upSpeed(self, up):
        self.speed += up

    def downSpeed(self, down):
        self.speed -= down
        if self.speed < 0:
            self.speed = 0

car1 = Car()
# 인스턴스 변수(필드)
print(car1.speed)
print(car1.color)

# 클래스 변수 num : 클래스 안에서 모든 인수들이 공유하는 변수
print(Car.number)

car2 = Car(10, 'Blue')
print(Car.number)