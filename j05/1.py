a = [1, 2.7, "ali", 4, 5, True, 7, 8, None, 10]
b = list((1, 2, 3, "rezaee", 5))
print(type(a))
print(type(b))

ali_rezaee_fname = "ali"
ali_rezaee_lname = "rezaee"
ali_rezaee_age = 30
ali_rezaee_phone = "09123456789"
ali_rezaee_address = "tehran,iran"

ali_rezaee = [ali_rezaee_fname, ali_rezaee_lname, ali_rezaee_age, ali_rezaee_phone, ali_rezaee_address]

ali_rezaee = ["ali", "rezaee", 30, "09123456789", "tehran,iran"]

for i in ali_rezaee:
    print(i, end=" ")