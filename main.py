import pprint
import pymongo as pymongo

def coonectdb():
    client = pymongo.MongoClient(
        "mongodb+srv://EpitaNoSQLDB:juyo7294@cluster0.w97ub.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test

    countries = db.countries
    continents = db.continents

    while(True):
        switch(countries,continents)


def switch(countries,continents):

    print()
    option = int(input("Enter The number of query you want to do:  "))

    if option == 1:
        ans = input("Enter the letters to search")
        query1(countries,ans)

    elif option == 3:
        query3(continents)

    elif option == 4:
        query4(continents,countries)

    elif option == 6:
        query6(countries)

    elif option == 7:
        query7(countries,"u", 100000)

    else:
        print("Incorrect option")


#------------------------
# POINT 1
# Send back all the country with a name started by a string given by the user
#------------------------
def query1(countries, letter):

    myquery = {"name": {'$regex': letter, '$options': "i"} }
    mydoc = countries.find(myquery)
    for countries in mydoc:
        pprint.pprint(countries)
        print()


#------------------------
# POINT 3
# Get all the continents with there number of countries
# ------------------------
def query3(continents):

    for continents in continents.find():
        print(continents["name"], len(continents["countries"]))
        print()


#------------------------
# POINT 4
# Send back the fourth countries of a continent bv alphabetic order (by country)
#------------------------
def query4(continents, countries):

    for continent in continents.find():
        id = continent["_id"]
        print(continent["name"])
        myquery = {"continent": id}
        sortCountries = countries.find(myquery).sort("name").limit(4)

        for x in sortCountries:
            pprint.pprint(x)
            print()

#------------------------
# POINT 6
# Get all the countries order by number of people first the less populated and last the most populated
#------------------------
def query6(countries):

    sortCountries = countries.find().sort("population")

    for country in sortCountries:
        pprint.pprint(country)
        print()

#------------------------
# POINT 7
# Get all the continents that have in their name a u and the population is bigger than 100,000
#------------------------
def query7(countries, letter, population):

    myquery = {"name": {'$regex': letter, '$options': "i"}, "population": { '$gte': population} }
    mydoc = countries.find(myquery)

    for countries in mydoc:
        pprint.pprint(countries)
        print()



if __name__ == '__main__':
    coonectdb()