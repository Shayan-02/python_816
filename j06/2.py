lst = [1, 2, 3, 4, 5]
lst[2] = "ali"
t = (1, 2, 3, 4, 5)

l = list(t)
l[2] = "reza"
t = tuple(l)
print(t)
