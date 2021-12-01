### This program is run by me at liamriley.hopto.org:5000 ###
from flask import Flask, jsonify, request

app = Flask(__name__)


### Converts capitals.db file into a list ###
def capital_list():
    countriesandcapitals = {}
    try:
        country_data = open('capitals.db', 'r')
    except IOError:
        print("Country list file could not be opened.")
        quit()
    try:
        for each_line in country_data:
            (country_name, capital_city) = each_line.split(':', 1)
            country_name = country_name.strip()
            capital_city = capital_city.strip()
            countriesandcapitals[country_name] = capital_city
        country_data.close()
        return countriesandcapitals
    except:
        pass


mycapitals = capital_list()


@app.route("/")
def hello_world():
    return "<p>Welcome to Liam's Country API!</p>"


@app.route("/findcapital")
def findcapital():
    if "country" in request.args:
        countryquery = request.args["country"]
        if countryquery in mycapitals:
            return jsonify(capital=mycapitals[countryquery])
        else:
            return "Oops, that country isn't in my list!"
    else:
        return "Oops, you didn't supply a country with your request!"


@app.route("/listcapitals")
def listcountries():
    return(jsonify(mycapitals))


app.run()
