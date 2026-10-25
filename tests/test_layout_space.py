from asciitree import LeftAligned
from asciitree.drawing import BoxStyle


def test_palette_without_space():
    """Custom palettes without a `SPACE` key retain ordinary space padding."""
    gfx = {
        "UP_AND_RIGHT": "+",
        "HORIZONTAL": "-",
        "VERTICAL": "|",
        "VERTICAL_AND_RIGHT": "+",
    }
    tree = {
        "root label": {
            "first label": {"first leaf": {}},
            "last label": {"last leaf": {}},
        },
    }
    expected = """root label
 +-- first label
 |   +-- first leaf
 +-- last label
     +-- last leaf"""
    assert LeftAligned(draw=BoxStyle(gfx=gfx))(tree) == expected
