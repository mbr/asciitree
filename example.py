from copy import deepcopy

from asciitree import LeftAligned
from asciitree.drawing import BoxStyle, BOX_DOUBLE, BOX_BLANK

tr = LeftAligned()

tree = {
    "asciitree": {
        "sometimes": {"you": {}},
        "just": {"want": {"to": {}, "draw": {}}},
        "trees": {},
        "in": {"your": {"terminal": {}}},
    }
}

print(tr(tree))

# construct a more complex tree by copying the tree and grafting it onto itself
tree2 = deepcopy(tree)
tree2["asciitree"]["trees"] = deepcopy(tree2["asciitree"])
print(tr(tree2))

# use a box style
box_tr = LeftAligned(draw=BoxStyle(gfx=BOX_DOUBLE, horiz_len=1))
print(box_tr(tree))

# more airy
air_tr = LeftAligned(
    draw=BoxStyle(gfx=BOX_BLANK, label_space=0, label_format="[{}]", indent=0)
)
print(air_tr(tree))
