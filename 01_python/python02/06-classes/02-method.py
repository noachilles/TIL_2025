# 인스턴스 메서드
class Person:
    def __init__(self, name):
        self.name = name
        print('인스턴스가 생성되었습니다.')
    def greeting(self):
        print(f'안녕하세요. {self.name}입니다.')
person1 = Person('지민')  # 인스턴스가 생성되었습니다.
person1.greeting()  # 안녕하세요. 지민입니다.


# 클래스 메서드
class Person:
    count = 0
    def __init__(self, name):
        self.name = name
        Person.count += 1
    @classmethod
    def number_of_population(cls):
        print(f'인구수는 {cls.count}입니다.')

person1 = Person('iu')
person2 = Person('BTS')



# 정적 메서드
class StringUtils:
    @staticmethod
    def reverse_string(string):
        return string[::-1]
    @staticmethod
    def capitalize_string(string):
        return string.capitalize()

text = 'hello, world'
reversed_text = StringUtils.reverse_string(text)
print(reversed_text)  # dlrow ,olleh
capitalized_text = StringUtils.capitalize_string(text)
print(capitalized_text)  # Hello, world
