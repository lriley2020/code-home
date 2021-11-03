"""
Seventh code@home homework task
"""
from statistics import multimode

nums = []
total = None


def askForNums():
    print("Please input your numbers below - press ctrl + c when finished")
    while True:
        try:
            newnum = int(input("> "))
            nums.append(newnum)
        except KeyboardInterrupt:
            break

    print("\nDone!")


def printMeanAvg():
    return sum(nums) / len(nums)


def printMedianAvg():
    sorted_nums = sorted(nums)
    middle = len(sorted_nums) // 2

    if len(sorted_nums) % 2 != 0:
        return sorted_nums[middle]

    return (sorted_nums[middle - 1] + sorted_nums[middle]) / 2


def printModeAvg():
    return multimode(nums)


askForNums()
print("Mean:")
print(printMeanAvg())
print("Median:")
print(printMedianAvg())
print("Mode")
print(printModeAvg())
