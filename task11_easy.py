countriesandcaptials = {"England": "London", "Russia": "Kiev", "France": "Paris"}

def menu():
    print("""
Please pick an option:
1) Add a country capital
2) Display all countries
3) See the capital of a specific country
4) Quit""")

while True:
    menu()
    choice = input("> ")
    if choice == "1":
        print("Enter a name followed by a country:"); countriesandcaptials[input("country> ").title()] = input("capital> ".title())
    elif choice == "2":
        for country in countriesandcaptials:
            print(f"{countriesandcaptials[country]} is the capital of {country}")
    elif choice == "3":
        query = input("country> ").title()
        if query in countriesandcaptials:
            print(f"{countriesandcaptials[query]} is the capital of {query}")
        else:
            print(f"Oops, {query} isn't in the list!")
    elif choice == "4":
        break
