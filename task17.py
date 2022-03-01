"""
Seventeenth code@home homework task
"""
unames = {"liam":"test", "bob":"password123"}
x = input("Username> ")
if x in unames and unames[x] == input("Password> "):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    while True:
        if 2 <= len(input("First Name> ")) <= 12 and 5 <= int(input("Age> ")) <= 60 and input("Favourite day of the week> ").title() in days: break
        else: print("Something is wrong, try again")
    print("Welcome!")
else: print("Access denied")