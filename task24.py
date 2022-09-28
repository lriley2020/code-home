import json

with open("average_numbers.json", "r+") as contents:
    numbers = json.load(contents)

def commit():
    with open("average_numbers.json", "w") as f:
        json.dump(numbers, f)

options = ["Smallest number", "Largest number", "Average", "Add number", "Quit"]
while True:
    for i in range(len(options)): print(f"{i+1}. {options[i]}")
    choice = int(input("choice> "))
    match choice:
        case 1: print(min(numbers))
        case 2: print(max(numbers))
        case 3: print(sum(numbers)/len(numbers))
        case 4: numbers.append(int(input("new number> "))); commit()
        case 5: raise SystemExit
