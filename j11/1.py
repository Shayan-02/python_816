a = ["ali", 2, 3 , 10, "reza", True]

b = [i for i in a if type(i) == int and i < 5]



l2 = ["1", "2", "3"]
c = [int(i) for i in l2]
print(c)


print(list(map(int, l2)))