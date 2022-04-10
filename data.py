rooms = {
    'Field': {
        'north': 'Playground',
        'south': 'Barn',
        'west': 'Forest',
        'items': [
            'stick'
        ],
        'description': 'A desolate field full of tall grass'
    },
    'Playground': {
        'south': 'Field'
    },
    'Barn': {
        'north': 'Field',
        'items': [
            'dog'
        ]
    },
    'Forest': {
        'east': 'Field'
    }
}