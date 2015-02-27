from asciitree import draw_tree


def test_behaves_as_originally_advertised():
    expected_output = """root
  +--sub1
  +--sub2
  |  +--sub2sub1
  +--sub3
     +--sub3sub1
     |  +--sub3sub1sub1
     +--sub3sub2"""

    class Node(object):
        def __init__(self, name, children):
            self.name = name
            self.children = children

        def __str__(self):
            return self.name

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

    assert draw_tree(root) == expected_output
