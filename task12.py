"""
Twelfth code@home homework task
"""

from random import randint

nextgame = "yes"
hasNotGuessed = True
gameno = 0
totalguesses = {}
while True:
    try:
        gameno += 1
        guesses = 0
        my_number = randint(0, int(input("number of numbers> ")))
        hasNotGuessed = True
        while hasNotGuessed:
            thisguess = int(input("guess> "))
            if my_number == thisguess:
                guesses += 1
                totalguesses[f"game{gameno}"] = guesses
                hasNotGuessed = False
                print("Correct!")
            else:
                guesses += 1
                print("That's not the number I'm thinking of!")
                bigger = True if thisguess < my_number else False
                if bigger:print("The number is bigger...")
                else:print("The number is smaller...")
    except KeyboardInterrupt:
        print("\nFinished game...")
        gameno -= 1
        break
print("----------------------------------------------------")
print("STATS")
print(f"You totalled {gameno} correct guesses out of {sum(totalguesses.values())} total quesses")
guessCorrectRatio = gameno / sum(totalguesses.values())
print(f"Your accuracy was {guessCorrectRatio * 100}%")
gamecount = 0
for score in totalguesses.values():
    gamecount += 1
    print(f"In game {gamecount} you took {score} guesses")
