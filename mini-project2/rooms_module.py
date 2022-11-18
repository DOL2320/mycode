# a dictionary linking a room to other rooms
# Add rooms, room descriptions, and list of items
rooms = {

    'Hall'        : {
        'south' : 'Kitchen',
        'east'  : 'Dining Room',
        'west'  : 'Library',
        'items' : [
            {
                'item': 'key',
                'description' : 'A copper key. Looks unremarkable, what could it open?'
            },
            {
                'item': 'coin',
                'description' : 'A gold coin.'
            }
        ],
        'desc'  : ''
    },

    'Library'     : {
        'north' : 'Study',
        'east'  : 'Hall',
        'desc'  : 'To the east is the Hall.\nTo the north is the Study.'
    },

    'Study'       : {
        'south' : 'Library',
        'desc'  : 'To the south is the Library.\nIn the center of the Study there is a desk with a typewriter.'
    },

    'Kitchen'     : {
        'north' : 'Hall',
        'enemy' : 'monster',
        'desc'  : ''
    },

    'Dining Room' : {
        'west'  : 'Hall',
        'south' : 'Garden',
        'items' : [
            {
                'item': 'potion',
                'description': ''
            }
        ],
        'desc'  : ''
    },

    'Garden'      : {
        'north' : 'Dining Room',
        'desc'  : ''
    }
}

print(rooms)
