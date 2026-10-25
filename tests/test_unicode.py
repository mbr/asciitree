from asciitree import LeftAligned


def test_unicode_doesnt_crash():
    tr = LeftAligned()
    assert tr({"åäö": {}}) == "åäö"
