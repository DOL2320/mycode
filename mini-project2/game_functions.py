#!/usr/bin/python3

from rooms_module import rooms

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    How to win:
      Get to the Garden with a key and a potion!
    How to lose:
      Avoid the monsters!
    ''')

def showStatus(currentRoom):
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the room description
    print(rooms[currentRoom]['desc'])
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "items" in rooms[currentRoom]:
        for item in rooms[currentRoom]['items']:
            print('You see a ' + item['item'])
    print("---------------------------")

def move(currentRoom, direction):
    #check that they are allowed wherever they want to go
    if direction in rooms[currentRoom]:
        #set the current room to the new room
        currentRoom = rooms[currentRoom][direction]
        return currentRoom
    # if they aren't allowed to go that way:
    else:
        print('You can\'t go that way!')

def get(currentRoom, item):
    # make two checks:
    # 1. if the current room contains an item
    # 2. if the item in the room matches the item the player wishes to get
    if "items" in rooms[currentRoom] and item in rooms[currentRoom]['items']:
        # add the item to their inventory
        inventory.append(item)
        # display a helpful message
        print(item + ' got!')
        # delete the item key:value pair from the room's dictionary
        del rooms[currentRoom]['items'][0]
    # if there's no item in the room or the item doesn't match
    else:
        #tell them they can't get it
        print('Can\'t get ' + item + '!')

def examine(currentRoom, item):
    # if the current room contains an item
    if "items" in rooms[currentRoom]:
        # Iterate through the list of items to find the name of the item to examine
        for item in rooms[currentRoom]['items']:
            # if item matches the item the player wishes to examine
            if action[1] == item['name']:
                # print the description of the item
                print(item['description'])
                
#def crushingWalls():
