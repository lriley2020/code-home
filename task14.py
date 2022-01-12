"""
Fourteenth code@home homework task
"""

def isLeapYear(leap):
    if leap % 4 == 0 and (leap % 100 != 0 or leap % 400 == 0):
        return True
    else:
        return False

def nextNLeaps(startyear, years):
    leaps = 0
    while leaps < years+1:
        startyear += 4
        if isLeapYear(startyear):
            print(startyear, end=" ")
            leaps += 1
    print()


while True:
    print("Enter a year to check")
    year = int(input("> "))
    if isLeapYear(year):
        print(f"{year} is a leap year!")
        print("These are the next 10 leap years:")
        nextNLeaps(year, 10)
    else:
        print("Not a leap year :(")
