# fib
# 1 1 2 3 5 8 13 21 ...
f1 = 1
f2 = 1
n = int(input("Enter a number: "))
if n == 1:
    print(f1)
elif n == 2:
    print(f1, f2)

elif n == 3:
    print(f1, f2, f1 + f2)

elif n == 4:
    print(f1, f2, f1 + f2, f2 + f1 + f2)
elif n == 5:
    print(f1, f2, f1 + f2, f2 + f1 + f2, f2 + f1 + f2 + f1 + f2)