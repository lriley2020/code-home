from bs4 import BeautifulSoup
from requests import get
import re

readnames = open("task18.db", "r").read().strip("\n").split()
newnames = list()
for name in readnames:
    if name.isalpha() and len(name) < 13:
        newnames.append(name)

r = get("https://metro.co.uk/2019/12/04/olivia-muhammad-top-list-popular-baby-names-2019-11266090/")
soup = BeautifulSoup(r.content, 'lxml')
divs = soup.find_all("div", class_="metro-factbox-content")
girlnames = list()
for li in divs[0].find_all('li'):
    girlnames.append(re.sub('<.*?>', '', str(li)))
boynames = list()
for li in divs[1].find_all('li'):
    boynames.append(re.sub('<.*?>', '', str(li)))

orderedgirls = list()
for popgirlname in girlnames:
    if popgirlname in newnames:
        orderedgirls.append(popgirlname)
        newnames.remove(popgirlname)

orderedboys = list()
for popboyname in boynames:
    if popboyname in newnames:
        orderedboys.append(popboyname)
        newnames.remove(popboyname)
print("These were the most popular boy names (in order): ")
for i in range(len(orderedboys)):
    print(f"{i+1}. {orderedboys[i]}")
print("These were the most popular girl names (in order): ")
for i in range(len(orderedgirls)):
    print(f"{i+1}. {orderedgirls[i]}")
print("These names did not appear in any of the lists: ")
for name in newnames:
    print(f"> {name}")