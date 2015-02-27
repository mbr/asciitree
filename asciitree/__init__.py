#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .drawing import BoxDraw
from .traversal import DictTraversal


class LeftAligned(object):
    draw = BoxDraw()
    traverse = DictTraversal()

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def render(self, node):
        lines = []

        children = self.traverse.get_children(node)
        lines.append(self.draw.node_label(self.traverse.get_text(node)))

        for n, child in enumerate(children):
            child_tree = self.render(child)

            if n == len(children) - 1:
                # last child does not get the line drawn
                lines.append(self.draw.last_child_head(child_tree.pop(0)))
                lines.extend(self.draw.last_child_tail(l)
                             for l in child_tree)
            else:
                lines.append(self.draw.child_head(child_tree.pop(0)))
                lines.extend(self.draw.child_tail(l)
                             for l in child_tree)

        return lines

    def __call__(self, tree):
        return '\n'.join(self.render(self.traverse.get_root(tree)))


# legacy support below

from .drawing import Draw
from .traversal import Traversal


class LegacyDraw(Draw):
    def node_label(self, text):
        return text

    def child_head(self, label):
        return '  +--' + label

    def child_tail(self, line):
        return '  |' + line

    def last_child_head(self, label):
        return '  +--' + label

    def last_child_tail(self, line):
        return '   ' + line


def draw_tree(node,
              child_iter=lambda n: n.children,
              text_str=str):
    """Support asciitree 0.2 API.

    This function solely exist to not break old code (using asciitree 0.2).
    Its use is deprecated."""
    traverse = Traversal()
    traverse.get_text = text_str
    traverse.get_children = child_iter

    return LeftAligned(traverse=traverse, draw=LegacyDraw())(node)
