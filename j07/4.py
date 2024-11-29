d = {1: "a", 2: "b", 3: "c", "asghar" : 50, True: "ali", None: "rezaee", "ali": "mohammadi"}

c = d.get(None)
print(c)

d.pop("asghar")
d.popitem()
print(d)
