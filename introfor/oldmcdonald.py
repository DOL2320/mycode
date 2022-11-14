#!/usr/bin/python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

## Part 1
# Store the agriculture array in a new variable to iterate through the list
ne_farm = farms[0]['agriculture']
print('The animals of the NE farm:')

# Iterate through the agriculture list and print the animals
for animal in ne_farm:
    print(' ', animal, sep='')
print()

## Part 2
# Ask the user to choose a farm
for farm in farms:
    print('-', farm['name'])
farm_choice = input('Choose a farm: ')

# Declare an empty list to store agriculture
farm_ag = []

# Loop through our list of farms
for farm in farms:
    # Use the farm choice to retrieve the correct farm 
    if farm['name'].lower() == farm_choice.lower():
        # Store the farms ag list in our variable
        farm_ag = farm['agriculture']

# Loop through the ag list and print
for ag in farm_ag:
    print(ag)

## Part 3
# Only return ANIMALS
