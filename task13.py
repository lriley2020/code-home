"""
Thirteenth code@home homework task
"""

kids = ["Ethan", "Jamie", "Aaron", "Alexander", "George", "Freya", "LiRi", "Toby", "LiRu", "Alfie", "Bobby",  "Zac", "Robert", "James", "Edward", "Archie", "Charlie", "Lincoln"]
good = {}
naughty = {}

for kid in kids:
    if input(f"Is {kid} good or naughty? (g/n): ") == "g": good[kid] = None
    else: naughty[kid] = "Coal"

for kid in good: good[kid] = input(f"What should {kid} get from santa?: ")
for kid,present in {**good, **naughty}.items(): print(f"{kid} is getting {present}")
print(f"{round(len(good)/len(kids)*100, 1)}% of the kids were good and {round(len(naughty)/len(kids)*100, 1)}% of the kids were naughty")
