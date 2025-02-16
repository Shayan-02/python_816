names = ["Alice", "Bob", "Charlie"]
ages = [24, 50, 18]

d = {}
for (name, age) in enumerate(zip(names, ages)):
    d[name] = age