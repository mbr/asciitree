# ASCII Trees

[![Run on Repl.it](https://repl.it/badge/github/mbr/asciitree)](https://repl.it/github/mbr/asciitree)

```text
asciitree
 +-- sometimes
 |   +-- you
 +-- just
 |   +-- want
 |       +-- to
 |       +-- draw
 +-- trees
 +-- in
     +-- your
         +-- terminal
```

```python
from asciitree import LeftAligned
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

tr = LeftAligned()
print(tr(tree))
```

Read the documentation at <https://pythonhosted.org/asciitree/>.
