class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
    
    def sayInfo(self):
        print(f"name: {self.name} \nage: {self.age}\njob: {self.job}")

    def move(self):
        pass


class Student(Person):
    def move(self, movement):
        print(f"{self.name} is {movement}")


class Baby(Person):
    def move(self, movement):
        print(f"{self.name} is {movement}")


s1 = Student("ali", 20, "student")
s1.sayInfo()
s1.move("walking")
s1.move("running")

b1 = Baby("reza", 1, "baby")
b1.sayInfo()
b1.move("4 dast o pa ing")