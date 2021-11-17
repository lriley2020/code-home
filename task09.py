"""
Ninth code@home homework task
"""

peopleandhobbies = {}
approved_hobbies = ["skateboarding", "cycling", "saxaphone"]
### Add the max no. of people below:
max_people = 5
people_added = 0

while people_added < max_people:
    try:
        print("Enter an name followed by a hobby:")
        name = input("> ")
        hobby = ""
        while hobby not in approved_hobbies:
            print("Enter a hobby  in this list:")
            print(approved_hobbies)
            hobby = input("> ").lower()
            if hobby not in approved_hobbies:
                print("Enter a hobby that is in the list and try again")
        peopleandhobbies[name] = hobby
        people_added += 1
        print(people_added)

    except KeyboardInterrupt:
        print("Done")
        break
if people_added == 6:
    print("Limit reached!")

for person in peopleandhobbies:
    print(f"{person} has the hobby of {peopleandhobbies[person]}")
