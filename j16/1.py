num1 = int(input("enter number1: "))
op = input("enter operator: ")
num2 = int(input("enter number2: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    try:
        print(num1 / num2)
    except ZeroDivisionError as z:
        raise z