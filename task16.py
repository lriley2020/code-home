"""
Sixteenth code@home homework task
"""
f = open("numbers.db", "r+")
def update_index():
    global scraped_nums
    scraped_nums = []
    f.seek(0)
    for num in f:
        scraped_nums.append(int(num))


update_index()
while True:
    choice = input("choice(view, add, count, largest, exit)> ")
    if choice == "view":
        print(*scraped_nums)
    if choice == "add":
        f.write(f"{input('number> ')}\n")
        f.flush()
        update_index()
    if choice == "count":
        print(len(scraped_nums))
    if choice == "largest":
        print(max(scraped_nums))
    if choice == "exit":
        f.close()
