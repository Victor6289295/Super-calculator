database = {
        "entrance": {
            "username": "ekuke",
            "password": "admin123",
            "intial_amount": 2000,
            "is_verified": True
            }
        }
command = input("select a command: ").lower().strip()
if command != ["Login", "Register", "Exit"]:
    print("Invalid Command")
elif command == "Register":
    print("Kindly fill the form to login or register")
    username = input("create username: ")
    if username in database:
        print(f"username, already exit")
    password = input("create password: ")
    intial_balance = float(input("deposit amount"))
    else:
        password = input("create password").strip()
        intial_amount = float(input(" "))
        is_verified = False
    user1 = {
        "username": username,
        "password": password,
        "intial_balance": intial_balance,
        "is_verified": False
            }
database.update(user1)
if choice = "yes" or "y"
    if initial >= fee
    intial_balance - fee
    print("")
