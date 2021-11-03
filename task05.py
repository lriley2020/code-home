"""
Fifth code@home homework task
"""

again = "yes"
times = 0
longest_name = ""
longest_value = 0
while again == "yes":
    print("Input a name below")
    name = input("> ")
    print(name.title() * len(name))

    if len(name) > longest_value:
        longest_name = name
        times += 1
        print("Again?")
        again = input("> ")
print(f"Run {times} times")
print(f"Longest name was '{longest_name}'")
