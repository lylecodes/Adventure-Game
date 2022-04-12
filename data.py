from characters import cellar_monster
from items import broken_tractor_blade, big_stick

rooms = {
    'Field': {
        'directions': {
            'north': 'Playground',
            'south': 'Barn',
            'east': 'Small Town',
            'west': 'Forest' 
        },
        'items': [
            big_stick
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
            'broken tractor': [
                broken_tractor_blade
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