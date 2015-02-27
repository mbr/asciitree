class Traversal(object):
    def get_children(self, node):
        raise NotImplementedError

    def get_root(self, tree):
        return tree

    def get_text(self, node):
        return str(node)


class DictTraversal(object):
    def get_children(self, node):
        return node[1].items()

    def get_root(self, tree):
        return tree.items()[0]

    def get_text(self, node):
        return node[0]
