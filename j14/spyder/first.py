class Person:
    def __init__(self, name="", age=1, job=""):
        self.name = name
        self.age = age
        self.job = job
    
    def introduce(self):
        return f"name: {self.name} \nage: {self.age} \njob: {self.job}"
    
    def move(self):
        pass


class Student(Person):
    def move(self, movement):
        return f"{self.name} is a {self.job} and it's movement is {movement}"


class Baby(Person):
    def move(self, movement):
        return f"{self.name} is a {self.job} and it's movement is {movement}"


class Employee(Person):
    def move(self, movement):
        return f"{self.name} is a {self.job} and it's movement is {movement}"


s1 = Student()