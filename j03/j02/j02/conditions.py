math = float(input("math: "))
physics = float(input("physics: "))
chemistry = float(input("chemistry: "))
geography = float(input("geography: "))
avg = (math + physics + chemistry + geography) / 4

if math > 20 or math < 0 or physics > 20 or physics < 0 or chemistry > 20 or chemistry < 0 or geography > 20 or geography < 0:
    print("false number")
elif avg >= 16:
    print("average is {} grade A".format(avg))
elif avg >= 12 and avg < 16:
    print("average is {} grade B".format(avg))
elif avg >= 10 and avg < 12:
    print("average is {} grade C".format(avg))
elif avg >= 0 and avg < 10:
    print("average is {} grade D ==> fail".format(avg))

