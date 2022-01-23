"""
Fourteen and a halfth code@home homework task
"""

from time import sleep
from random import choice

kidjokes = {"Why did a scarecrow win a Nobel prize?": "He was outstanding in his field!",
            "What do sprinters eat before a race?": "Nothing. They fast!",
            "What do you do when a lemon gets sick?": "You give it lemon-aid."}
adultjokes = {"Did you hear about the first restaurant to open on the moon?": "It had great food, but no atmosphere.",
              "Why should you never trust stairs?": "They’re always up to something.",
              "Why are toilets always so good at poker?": "They always get a flush"}

def askjoke(joke, punchline, delay):
    print(joke)
    sleep(delay)
    print(punchline)

while True:
    print("Enter your age below:")
    if int(input("> ")) < 18:
        randomjoke = choice(list(kidjokes))
        askjoke(randomjoke, kidjokes[randomjoke], 3)
    else:
        randomjoke = choice(list(adultjokes))
        askjoke(randomjoke, adultjokes[randomjoke], 3)
    print("*uproarious laughter*")
