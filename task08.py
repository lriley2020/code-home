from random import choice
from time import sleep
from datetime import datetime

allowed_users = {}

print("Please input the desired users below - type \"done\" when finished")
while True:
    try:
        newmember = input("> ")
        nums = "0123456789"
        token = ""
        for i in range(5):
            token += choice(nums)
        allowed_users[int(token)] = newmember
        print(f"{newmember}'s access token is {token}")
        log = open("club_auth.log", "a")
        log.write(f"{datetime.now().strftime('%H:%M:%S')}  Added new user \"{newmember}\"\n")
        log.flush()
    except KeyboardInterrupt:
        break

print("\nMember list generated...")

while True:
    print("Enter your access token below:")
    user_input = int(input("> "))
    if user_input in allowed_users:
        print(f"Welcome back, {allowed_users[user_input]}")
        log.write(f"{datetime.now().strftime('%H:%M:%S')}  User \"{allowed_users[user_input]}\" has logged in... \n")
        log.flush()
        sleep(2)
        print("Logging out...")
        log.write(f"{datetime.now().strftime('%H:%M:%S')}  User \"{allowed_users[user_input]}\" has logged out... \n")
        log.flush()
    else:
        print("Back off stranger!")
        log.write(f"{datetime.now().strftime('%H:%M:%S')}  Failed login with key \"{user_input}\" \n")
        log.flush()
