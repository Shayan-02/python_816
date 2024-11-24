sum, max = 0, 0
lst = []
a = input().split()
min = float(a[0])
for i in a:
    if 0 <= float(i) <= 20:
        lst.append(float(i))
        sum += float(i)
        if max < float(i):
            max = float(i)
        if min > float(i):
            min = float(i)
print(sum/len(lst), max, min, end="\n")