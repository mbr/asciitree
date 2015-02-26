#!/usr/bin/env python
# -*- coding: utf-8 -*-

from legacy import draw_tree, _draw_tree


def ascii_tree(node,
               get_node_children=lambda t: t[1].items(),
               get_node_text=lambda t: t[0],
               get_root=lambda d: d.items()[0]):
    return _draw_tree(get_root(node), '', get_node_children, get_node_text)
