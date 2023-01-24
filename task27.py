import matplotlib.pyplot as plt

seq = input("Enter a string of text> ").lower()

while True:
    searches = input("Letters to search for> ").split()
    if not searches: break
    results = []
    for search in searches:
        times = seq.count(search)
        print(f"The letter {search} appeared in the string {times} times")
        results.append(times)
    if input("Show graph (y/n)?> ") == "y":
        plt.bar(searches, results)
        plt.show()
