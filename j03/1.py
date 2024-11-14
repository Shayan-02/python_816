num1 = int(input("enter number1: "))
op = input("enter operator: ")
num2 = int(input("enter number2: "))

if op == "+":
    print(f"sum of {num1} and {num2} is {num1+num2}")
elif op == "-":
    print(f"sub of {num1} and {num2} is {num1-num2}")
elif op == "*":
    print(f"mul of {num1} and {num2} is {num1*num2}")
elif op == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print(f"div of {num1} and {num2} is {num1/num2}")
else:
    print("invalid operator")
