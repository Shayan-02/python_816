d = {1:"a", 2:"b", 3:"c"}

for key, value in d.items():
    print(key, value)

d.update({4:"d"})

d[3] = "cc"

for key, value in d.items():
    print(key, value)
    
if 1 not in d:
    d[1] = "b"
else:
    pass