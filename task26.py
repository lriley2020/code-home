from random import sample, randint

### Generate a random list of unique numbers for the program to sort ###
### There's probably a more efficient way to do this in python using fancy maths###
thelist = sample(range(0,1000000),1000000)


x = int(input("search> "))

hasFound = False
for i in range(len(thelist)):
    if thelist[i] == x:
        print(f"Found at index {i}")
        hasFound = True
        break

if not hasFound: print("Not found")