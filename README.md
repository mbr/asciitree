# ASCII Trees

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

tree = {
    "asciitree": {
        "sometimes": {"you": {}},
        "just": {"want": {"to": {}, "draw": {}}},
        "trees": {},
        "in": {"your": {"terminal": {}}},
    }
}

tr = LeftAligned()
print(tr(tree))
```

Since Python 3.7, dictionaries preserve insertion order. On older versions, use
`collections.OrderedDict` to preserve the tree's display order.

Read the documentation at <https://asciitree.readthedocs.io/en/stable/>.
