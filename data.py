from characters import cellar_monster

rooms = {
    'Field': {
        'directions': {
            'north': 'Playground',
            'south': 'Barn',
            'east': 'Small Town',
            'west': 'Forest' 
        },
        'items': [
            'big stick'
        ],
        'description': '"A desolate field full of tall grass"'
    },
    'Playground': {
        'directions': {
            'south': 'Field' 
        },
        'description': '"A playground with rusted play equipment"'
    },
    'Barn': {
        'directions': {
            'north': 'Field',
            'south': 'Cellar',
        },
        'searchables': {
            'tractor': [
                'broken blade'
            ]
        },
        'description': '"A smelly old barn with a broken tractor"'
    },
    'Forest': {
        'directions': {
            'east': 'Field'
        },
        'description': 'An endless sea of trees'
    },
    'Cellar': {
        'directions': {
            'north': 'Barn'
        },
        'npcs': [
            cellar_monster
        ],
        'description': '"As you stand in pure darkness, you hear a low growl"'
    },
    'Small Town': {
        'directions': {
            'west': 'Field'    
        },
        'items': {},
        'npcs': [],
        'description': "An abandoned town with a few buildings"
    }
}