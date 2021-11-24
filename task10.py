"""
Tenth code@home homework task
"""
from sys import exit
evens = 0
odds = 0
while True:
    option = input("option> ")
    if option == "add numbers":
        try:
            inputted = int(input("number> "))
            evens, odds = (evens + 1, odds) if inputted % 2 == 0 else (evens, odds + 1)

        except KeyboardInterrupt:
            break
    if option == "quit": exit()
    if option == "see numbers": print(f"There were {evens} evens and {odds} odds")
