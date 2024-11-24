a = [1, 2.7, "ali", 4, 5, True, 7, 8, None, 10]
b = [1, 2, 3]

b.append(4)
b.append(0)

b.insert(2, "rezaee")

b.extend(a)
print(b)

a.pop()
a.pop(3)
a.remove("ali")
# a.clear()

c = a.copy()
print(a)
print(c)

d = list(a)
print(d)

a[5] = "asghar"
