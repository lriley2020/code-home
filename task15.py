f = open("names.db", "r+")
def getValidAge():
    while True:
        age = int(input("age> "))
        if 5 <= age <= 25:
            return age
        print("That age is not valid, please try again")

def getValidName():
    while True:
        name = input("name> ")
        if 1 < len(name) < 20:
            return name
        print("Looks like that name  was too long, please try again")

def orderedAges():
    ages = {}
    f.seek(0)
    for line in f.readlines():
        age = int(line.split(":")[1])
        if age in ages:
            ages[age] += 1
        else:
            ages[age] = 1
    ordered = []
    for key, val in list(ages.items()):
        ordered.append((val, key))
    ordered.sort(reverse=True)
    for count,age in ordered:
        print(f"{count} {'people' if count>1 else 'person'} had the age of {age}")


while True:
    print("What would you like to do?")
    choice = input("choice (add, view, popular)> ")
    if choice == "add":
        f.write(f"{getValidName()}:{getValidAge()}\n")
        f.flush()
    elif choice == "view":
        f.seek(0)
        for line in f.readlines(): print(line.replace(":", " is ").strip("\n"))
    elif choice == "popular":
        orderedAges()