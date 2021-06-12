# 클래스 상속 실습
# 슈퍼클래스 : 사람 클래스 Person <- 서브클래스 : 학생 클래스 Student
class Person:
    def __init__(self, age, sex, name):
        self.age = age
        self.name = name
        self.sex = sex

    def greeting(self):
        print('안녕하세요~')

class Student(Person):
    # 학교, 학과, 학번, 공부를 하다(), 시험을 보다()
    def __init__(self, age, sex, name, school, major, stu_num):
        super().__init__(age, sex, name)
        self.school = school
        self.major = major
        self.stu_num = stu_num

    def study(self):
        print(f'{self.name}은/는 {self.school}에서 공부를 하고, 학번은 {self.stu_num}이다.')

    def exam(self):
        print(f'{self.name}이/가 {self.major} 시험을 본다.')

stu1 = Student('23', '남', '홍길동', '고려대', '체육학과', '123')
stu2 = Student('20', '여', '유관순', '연세대', '역사학과', '456')

stu1.greeting() ; stu2.greeting()

stu1.study() ; stu1.exam()
stu2.study() ; stu2.exam()