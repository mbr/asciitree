#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


def draw_tree(node,
              child_iter=lambda n: n.children,
              text_str=str):
    # this method is kept around for backwards compatibility - existing code
    # will call draw tree. do not use this in new code
    return _draw_tree(node, '', child_iter, text_str)


def ascii_tree(node,
               get_node_children=lambda t: t[1].items(),
               get_node_text=lambda t: t[0],
               get_root=lambda d: d.items()[0]):
    return _draw_tree(get_root(node), '', get_node_children, get_node_text)


def _draw_tree(node, prefix, child_iter, text_str):
    buf = StringIO()

    children = list(child_iter(node))

    # check if root node
    if prefix:
        buf.write(prefix[:-3])
        buf.write('  +--')
    buf.write(text_str(node))
    buf.write('\n')

    for index, child in enumerate(children):
        if index+1 == len(children):
            sub_prefix = prefix + '   '
        else:
            sub_prefix = prefix + '  |'

        buf.write(
            _draw_tree(child, sub_prefix, child_iter, text_str)
        )

    return buf.getvalue()


if __name__ == '__main__':
    nodes = {
        'root': {
            'sub1': {},
            'sub2': {
                'sub2sub1': {}
            },
            'sub3': {
                'sub3sub1': {
                    'sub3sub1sub1': {}
                },
                'sub3sub2': {}
            }
        }
    }

    print ascii_tree(nodes)
