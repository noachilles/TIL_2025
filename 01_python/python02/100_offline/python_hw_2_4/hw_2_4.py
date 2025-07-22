class Animal():
    
    def __init__ (self, name):
        self.name = name
        
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
class Flyer():
    def fly(self):
        return "Flying"
    
class Swimmer():
    def swim(self):
        return "Swimming"
    
class Duck(Flyer, Swimmer, Animal):
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Quack!"
    
def make_animal_speak(animal):
    print(animal.speak())

if __name__ == "__main__":
    cat = Cat("cat")
    dog = Dog("dog")
    duck = Duck("duck")

    make_animal_speak(cat)
    make_animal_speak(dog)
    make_animal_speak(duck)
    print(duck.fly())
    print(duck.swim())