"""This module is kept around mimic the old implementation of asciitree. As
asciitree is (or at least used to be) a very small module, one cannot
reasonably expect anyone to update an application solely because asciitree's
API changed.

All everything in this module is imported into the asciitree module namespace
and will cause things to keep working as advertised.
"""

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


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
