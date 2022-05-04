import matplotlib.pyplot as plt

scores = []

while True:
    name = input("player name>")
    if name == "": break
    elif len(name) > 10: print("Name too long"); continue
    score = int(input("score> "))
    if not (0 < score <= 100): print("Score too large"); continue
    scores.append((name, score))

x,y = zip(*scores)

plt.bar(x,y)
plt.show()
