n1 = "ali"
try:
    print(10/0)
    print(int(n1))
except ZeroDivisionError:
    print("mamad az madreseh oomad")
except Exception as e:
    print(e)
else:
    print("mamad")
finally:
    print("rezaee")


