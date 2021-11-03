"""
Fourth code@home homework task
"""

print("Welcome to the NameCheck utility")
again2 = "yes"

while again2 == "yes":
    names = []
    again = "yes"
    maxlen = 0
    maxname = ""
    while again == "yes":
        print("Enter a name below:")
        name = input("> ")
        if len(name) > maxlen:
            maxlen = len(name)
            maxname = name
        print("Enter another name? (yes/no)")
        again = input("> ")
    print(f"'{maxname}' is bigger")
    print("Run again (yes/no)?")
    again2 = input("> ")
