for i in range(1, 25):
    if i == 14 or i == 17:
        i += 2
        continue
    if i == 20:
        break
    print(i)