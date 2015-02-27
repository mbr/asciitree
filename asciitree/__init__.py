#!/usr/bin/env python
# -*- coding: utf-8 -*-

from legacy import draw_tree, _draw_tree


def left_aligned(tree,
                 get_node_children=lambda t: t[1].items(),
                 get_node_text=lambda t: t[0],
                 get_root=lambda d: d.items()[0]):
    return '\n'.join(_left_aligned(get_root(tree),
                     get_node_children,
                     get_node_text))


def _left_aligned(node, get_node_children, get_node_text):
    lines = []

    children = get_node_children(node)
    lines.append(get_node_text(node))

    for n, child in enumerate(children):
        child_tree = _left_aligned(child, get_node_children, get_node_text)

        if n == len(children) - 1:
            # last child does not get the line drawn
            lines.append('  +--' + child_tree.pop(0))
            prefix = '   '
        else:
            lines.append('  +--' + child_tree.pop(0))
            prefix = '  |'

        child_tree = [prefix + l for l in child_tree]
        lines.extend(child_tree)

    return lines
