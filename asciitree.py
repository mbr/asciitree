#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

class Node(object):
    def __init__(self, name, children):
        self.name = name
        self.children = children

    def __str__(self):
        return self.name

    # Call it with a collections.OrderedDict if node order
    # is important!
    # Also, there can only be one root node.
    @classmethod
    def from_dictionary(cls, node_dictionary):
        def loop(nodes):
            node_list = []
            for name, children in nodes.iteritems():
                if children:
                    node_list.append(cls(name,
                                         loop(children)))
                else:
                    node_list.append(cls(name, []))

            return node_list

        return loop(node_dictionary)[0]

def draw_tree(node,
              child_iter=lambda n: n.children,
              text_str=str):
    return _draw_tree(node, '', child_iter, text_str)


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
    print "Example #1:"

    root = Node('root', [
        Node('sub1', []),
        Node('sub2', [
            Node('sub2sub1', [])
        ]),
        Node('sub3', [
            Node('sub3sub1', [
                Node('sub3sub1sub1', [])
            ]),
            Node('sub3sub2', [])
        ])
    ])

    print draw_tree(root)

    print "Example #2:"

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

    print draw_tree(Node.from_dictionary(nodes))

