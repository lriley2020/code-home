peopleandhobbies = {}
approved_hobbies = ["skateboarding", "cycling", "saxaphone"]

while True:
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
  except KeyboardInterrupt:
    print("Done")
    break

for person in peopleandhobbies:
  print(f"{person} has the hobby of {peopleandhobbies[person]}")
