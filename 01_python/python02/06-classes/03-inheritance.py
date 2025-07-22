class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def talk(self):  # 메서드 재사용
        print(f'반갑습니다. {self.name}입니다.')
class Professor(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)
# 부모 Person 클래스의 talk 메서드를 활용
p1.talk()  # 반갑습니다. 박교수입니다.
# 부모 Person 클래스의 talk 메서드를 활용
s1.talk()  # 반갑습니다. 김학생입니다.


# 다중 상속 예시
class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        return f'안녕, {self.name}'
class Mom(Person):
    gene = 'XX'
    def swim(self):
        return '엄마가 수영'
class Dad(Person):
    gene = 'XY'
    def walk(self):
        return '아빠가 걷기'

class FirstChild(Dad, Mom):
    def swim(self):
        return '첫째가 수영'
    def cry(self):
        return '첫째가 응애'
baby1 = FirstChild('아가')
print(baby1.cry())  # 첫째가 응애
print(baby1.swim())  # 첫째가 수영
print(baby1.walk())  # 아빠가 걷기
print(baby1.gene)  # XY
