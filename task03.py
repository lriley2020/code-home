"""
Third code@home homework task
"""

print("Welcome to Liam Riley's Amazing Calculator!")


### calculation function ###
def askfunction():
    print("Enter your calculation below: (multiply=*, divide=/)")
    calc = input("> ")
    try:
        print(eval(calc))
    except SyntaxError:
        print(f"Ooops - it looks like your calculation, '{calc}', was invalid!")
    print("Would you like to do another calculation? (y/n)")
    response = input("> ")
    if response == "y":
        askfunction()


askfunction()
