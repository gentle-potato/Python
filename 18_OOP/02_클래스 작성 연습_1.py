########## 연습문제 ##########
print('\n########## 연습문제 ##########')
class Dog :
    def __init__(self, Breed, Size, Age, Color):
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

dog1 = Dog('Neapolitan Mastiff', 'Large', '5 years', 'Black')
dog2 = Dog('Maltese', 'Small', '2 years', 'White')
dog3 = Dog('Chow Chow', 'Medium', '3 years', 'Browm')

print('\n=== showInfo() ===')
dog1.showInfo() ; dog2.showInfo() ; dog3.showInfo()

print('\n=== 행동 ===')
dog1.Eat() ; dog1.Sleep() ; dog1.Sit() ; dog1.Run()
dog2.Eat() ; dog2.Sleep() ; dog2.Sit() ; dog2.Run()
dog3.Eat() ; dog3.Sleep() ; dog3.Sit() ; dog3.Run()