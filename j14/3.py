class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def move(self):
        pass

class Student(Person):
    def move(self, movement):
        return f"{self.name} is {movement}ing..."


class Baby(Person):
    def move(self, movement):
        print(f"{self.name} is {movement}ing...")


s1 = Student()