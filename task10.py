"""
Tenth code@home homework task
"""
evens = 0; odds = 0
while True:
    option = input("option> ")
    if option == "add numbers":
        inputted = int(input("number> "))
        evens, odds = (evens + 1, odds) if inputted % 2 == 0 else (evens, odds + 1)
    if option == "quit": break
    if option == "see numbers": print(f"There were {evens} evens and {odds} odds")
    else: print("Oops, that's not a valid option!")
