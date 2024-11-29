dict1 = {"name" : "ali", "age" : 25, "address" : "tehran", "phone" : "09123456789"}
print(dict1)
# print(dict1.keys(), dict1.values())
for i in dict1:
    print(i, ":", dict1[i])

for i in dict1.items():
    print(i)