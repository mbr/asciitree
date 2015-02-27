from asciitree import ascii_tree
from collections import OrderedDict as OD


tree = {
    'asciitree': OD([
        ('sometimes',
            {'you': {}}),
        ('just',
            {'want': OD([
                ('to', {}),
                ('draw', {}),
            ])}),
        ('trees', {}),
        ('in', {
            'your': {
                'terminal': {}
            }
        })
    ])
}

print ascii_tree(tree)
