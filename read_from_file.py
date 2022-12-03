import json

f = open('country-by-languages.json')
countries_json = f.read()
countries = json.loads(countries_json)

# print(countries)