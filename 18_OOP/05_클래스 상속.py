# 클래스 상속(inheritance)
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

class Truck(Car):
    def __init__(self, speed, color, load):
        super().__init__(speed, color)   # 부모 객체 사용
        self.load = load   # 트럭 클래스의 필드 추가

    # 메소드를 재정의 : 오바라이딩(overriding)
    def showLoad(self):
        print(self.load)

    def upLoad(self, up):
        self.load += up

    def showInfo(self):
        print('Truck : 속도는 %d이고, 적재량은 %d입니다.' % (self.speed, self.load))

car1 = Car()
car2 = Truck(0, 'Blue', 1000)

car1.showInfo()
car2.showInfo()
car2.showLoad()
car2.upSpeed(10)
car2.showInfo()

print(isinstance(car2, Car))
print(issubclass(Truck, Car))
print(issubclass(bool, int))

class SportCar(Car):
    def __init__(self, speed, color, seats):
        super().__init__(speed, color)
        self.seats = seats

    def showInfo(self):
        print('Sport Car : 색상은 %s, 좌석수는 %d' % (self.color, self.seats))

car3 = SportCar(0, 'Red', 2)
car3.showInfo()

# 다형성(polymorphism) : 동일한 이름의 메소드이지만, 다른 기능을 수행
carL = [car1, car2, car3]

for car in carL:
    car.showInfo()