#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

import game_functions

# an inventory, which is initially empty
inventory = []

# start the player in the Hall
currentRoom = 'Hall'

game_functions.showInstructions()

# breaking this while loop means the game is over
while True:
    game_functions.showStatus(currentRoom)

    # the player MUST type something in
    # otherwise input will keep asking
    action = ''
    while action == '':  
        action = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    action = action.lower().split(" ", 1)

    #if they type 'go' first
    if action[0] == 'go':
        move(currentRoom, action[1])

    #if they type 'get' first
    if action[0] == 'get':
        get(currentRoom, action[1])

    # If the user types 'examine' first
    if action[0] == 'examine':
        examine(currentRoom, action[1])

    ## If a player enters a room with a monster
    if 'items' in rooms[currentRoom]:
        for item in rooms[currentRoom]['items']:
            if item['name'] == 'monster':
                print('A monster has got you... GAME OVER!')
                break

    ## If a player enters the garden with the key and the potion, they win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
