"""
Fourteenth code@home homework task
"""

def isLeapYear(leap):
    if leap % 4 == 0 and (leap % 100 != 0 or leap % 400 == 0):
        return True
    else:
        return False

def next10Leaps(startyear):
    leaps = 0
    while leaps < 11:
        startyear += 4
        if startyear % 4 == 0 and (startyear % 100 != 0 or startyear % 400 == 0):
            print(startyear, end=" ")
            leaps += 1
    print()


while True:
    print("Enter a year to check")
    year = int(input("> "))
    if isLeapYear(year):
        print(f"{year} is a leap year!")
        print("These are the next 10 leap years:")
        next10Leaps(year)
    else:
        print("Not a leap year :(")
