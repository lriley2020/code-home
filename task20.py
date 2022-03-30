import json

def yes():
    n1 = input("first name> "); print("odd" if len(n1) % 2 != 0 else "even")
    n2 = input("second name> "); print("odd" if len(n2) % 2 != 0 else "even")
    with open("names.json", "r+") as names:
        contents = json.load(names)
        contents.append(f"{n1} {n2}")
        names.seek(0)
        json.dump(contents, names)

yes()