"""Exercício 39 - Dictionaries, Oh Lovely Dictionaries"""


#  create a mapping of state to abbreviation
states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CA',
        'Michigan': 'MI'
        }

#  Create a basic set of states and some cities in them
cities = {
        'CA': 'San Francisco',
        'MI': 'Detroid',
        'FL': 'Jacksonvile'
        }

#  Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#  Print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#  Print some states.
print('-' * 10)
print("Michigan's abbreviattion is: ", states['Michigan'])
print("Florida's abbreviation: ", states['Florida'])

#  do it using the state then cities dict
print('-' * 10)
print('Michigan has: ', cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#  print every state abbreviation
print('-' * 10)
print(states.items())
for state, abrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print everty city in state
print('-' * 10)
for abrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(cities.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"ans has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city =cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")

