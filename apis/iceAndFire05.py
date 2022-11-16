#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
    ## Ask user for input
    got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

    ## Send HTTPS GET to the API of ICE and Fire character resource
    res = requests.get(AOIF_CHAR + got_charToLookup).json()

    character_name = res['name'] 
    print(f'Name: {character_name}')
    print('Affiliated houses:')

    # loop through the houses and retrieve the data
    for item in res['allegiances']:
        HOUSE_URL = item
        house_res = requests.get(HOUSE_URL).json()
        print(' - ' + house_res['name'])

    print('Books:')

    for book in res['books']:
        BOOK_URL = book
        book_res = requests.get(BOOK_URL).json()
        print(' - ' + book_res['name'])

if __name__ == "__main__":
        main()

