names = list()
with open("namegame.db", "r") as f:
    for name in f: names.append(name.strip("\n"))
    while True:
        name = input("name> ").title()
        if name not in names: break
        print("Sorry, that name has already been used!")
vowels = ["A", "E", "I", "O", "O"]
if name[0] not in vowels: newname = name[1:]
else: newname = name
again = "y"
while again == "y":
    print(f"""{name}, {name}, bo{'-b' if name[0] != 'B' else '-'}{newname.lower()},
    Bonana-fanna fo{'-f' if name[0] != 'F' else '-'}{newname.lower()},
    Fee fi mo-m{'-m' if name[0] != 'M' else '-'}{newname.lower()},
    {name}!""")
    again = input("again?(y/n)> ")
with open("namegame.db", "a") as f:
    f.write(f"{name}\n")
