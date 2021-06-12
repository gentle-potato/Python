########## 연습문제 ##########
print('\n########## 연습문제 ##########')
class Dog :
    def __init__(self, Name, Breed, Size, Age, Color):
        self.Name = Name
        self.Breed = Breed
        self.Size = Size
        self.Age = Age
        self.Color = Color
    def showInfo(self):
        print('Breed : %s\nSize : %s\nAge : %s\nColor : %s' % (self.Breed, self.Size, self.Age, self.Color))

    def Eat(self):
        print(f'{self.Breed}가 먹는다.')

    def Sleep(self):
        print(f'{self.Breed}가 잔다.')

    def Sit(self):
        print(f'{self.Breed}가 앉는다.')

    def Run(self):
        print(f'{self.Breed}가 달린다.')

    def __str__(self):
        return print(f'이름 : {self.Name}, 나이 : {self.Age}, 종류 : {self.Breed}')

    def __lt__(self, other):
        if self.Age < other.Age:
            print(f'{self.Name}가 {other.Name}보다 나이가 어립니다.')
        elif self.Age > other.Age:
            print(f'{self.Name}가 {other.Name}보다 나이가 많습니다.')
        else :
            pass
        return self.Age < other.Age

    def __eq__(self, other):
        if self.Age == other.Age:
            print(f'{self.Name}와 {other.Name}는 나이가 같습니다.')
        else :
            print(f'{self.Name}와 {other.Name}는 나이가 다릅니다.')
        return self.Age == other.Age

dog1 = Dog('하나', 'Neapolitan Mastiff', 'Large', '5 years', 'Black')
dog2 = Dog('두리', 'Maltese', 'Small', '2 years', 'White')
dog3 = Dog('세찌', 'Chow Chow', 'Medium', '3 years', 'Browm')

print('\n=== showInfo() ===')
dog1.showInfo() ; dog2.showInfo() ; dog3.showInfo()

print('\n=== 행동 ===')
dog1.Eat() ; dog1.Sleep() ; dog1.Sit() ; dog1.Run()
dog2.Eat() ; dog2.Sleep() ; dog2.Sit() ; dog2.Run()
dog3.Eat() ; dog3.Sleep() ; dog3.Sit() ; dog3.Run()

print('\n=== __str__() ===')
dog1.__str__() ; dog2.__str__() ; dog3.__str__()
print('\n=== __lt__(other) ===')
dog1.__lt__(dog2) ; dog1.__lt__(dog3)
dog2.__lt__(dog3) ; dog2.__lt__(dog1)
dog3.__lt__(dog1) ; dog3.__lt__(dog2)
print('\n=== __eq__(other) ===')
dog1.__eq__(dog2) ; dog1.__eq__(dog3)
dog2.__eq__(dog3) ; dog2.__eq__(dog1)
dog3.__eq__(dog1) ; dog3.__eq__(dog2)