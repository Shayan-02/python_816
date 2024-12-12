from random import *
# s = int(input())
# e = int(input())
# a = randint(s, e)
# print(a)
def rps(user:str) -> str:
    choices = ["r", "p", "s"]
    c_choice = choice(choices)
    if user == c_choice:
        return "مساوی"
    elif user == "p" and c_choice == "r":
        return "بردی"
    elif user == "p" and c_choice == "s":
        return "باختی"
    elif user == "s" and c_choice == "p":
        return "بردی"
    elif user == "s" and c_choice == "r":
        return "باختی"
    elif if user == "r" and c_choice == "p":
        return "باختی"
    elif user == "r" and c_choice == "s":
        return "بردی"

u1 = input("r, p, s: ")
print(rps(u1))