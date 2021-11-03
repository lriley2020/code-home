"""
The first homework task for y10 computer science
"""
from time import sleep

mystr = "Hi! This is a program to show you that I am ready to program at home!"


def slow_print(text):
    for letter in text:
        sleep(0.05)
        print(letter, end='', flush=True)


slow_print(mystr)
