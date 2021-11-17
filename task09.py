peopleandhobbies = {}

while True:
  try:
    print("Enter an name followed by a hobby:")
    name = input("> ")
    hobby = input("> ")
    peopleandhobbies[name] = hobby
  except KeyboardInterrupt:
    print("Done")
    break

for person in peopleandhobbies:
  print(f"{person} has the hobby of {peopleandhobbies[person]}")
