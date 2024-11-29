employees = {
    "ali_rezaee": {
        "name": {"fname": "ali", "lname": "rezaee"},
        "age": 25,
        "address": "tehran",
        "phone": {"mobile": "09123456789", "home": "02123456789"},
        "hobbies" : ["watching movies", "playing games"]
    },
    "ali_mohammadi": {
        "name": {"fname": "ali", "lname": "mohammadi"},
        "age": 30,
        "address": "tehran",
        "phone": {"mobile": "0987654321", "home": "02123456789"},
    },
}

print(employees["ali_mohammadi"]["phone"]["mobile"])
