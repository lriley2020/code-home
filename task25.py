from json import load, dump
from random import choice
from calendar import month_name

with open("greetings.db") as f:
    greetings = load(f)

months = month_name[1:]

notValid = True
while notValid:
    name = input("name> ")
    if not 2 < len(name) < 10:
        continue
    age = int(input("age> "))
    if not 5 < age <= 65:
        continue
    month = input("month of birth> ").title()
    if month not in months:
        continue
    notValid = False

print(choice(greetings))

with open("name.db", "r+") as f:
    thelist = load(f)
    thelist.append([name, age, month])
    f.seek(0)
    dump(thelist, f)

