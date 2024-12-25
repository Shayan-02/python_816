from first import *

s1 = Student("ali", 20, "student")
print(s1.introduce())
print(s1.move(input("enter the movement type: ")))

b1 = Baby("reza", 1, "baby")

print(b1.introduce(), b1.move(input("enter the movement type: ")), sep="\n")

