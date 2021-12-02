import requests

server_string = "http://liamriley.hopto.org:5000"

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
        print("Sorry, the list of countries is currently complete!")
    elif choice == "2":
        ### Get all countries and capitals from the API and convert them from json to a dict ###
        r = requests.get(f"{server_string}/listcapitals")
        countriesandcapitals = r.json()
        for country in countriesandcapitals:
            print(f"{country} has the capital of {countriesandcapitals[country]}")
    elif choice == "3":
        ### Ask the user for a country then query the API for it and convert the response from json ###
        ### If this fails, display an error message ###
        query = input("country> ").title()
        r = requests.get(f"{server_string}/findcapital?country={query}")
        try:
            data = r.json()
            capital = data["capital"]
            print(f"{query} has the capital of {capital}")
        except:
            print("Oops, it looks like your country was not recognised!")
    elif choice == "4":
        break
