"""Tree class and tree node class."""


class Node(object):
    """Node in a tree."""

    def __init__(self, data, children=None):
        children = children or []
        assert isinstance(children, list), \
            "children must be a list!"
        self.data = data
        self.children = children

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Node %s>" % self.data

    def get_num_children(self):
        """Get number of children.

        For example::

            >>> a = Node("A", [Node("B"), Node("C")])
            >>> a.get_num_children()
            2
        """

        return len(self.children)


class Tree(object):
    """Tree."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Tree root=%s>" % self.root

    def depth_first_search(self, data):
        """Return node object with this data, traversing the tree depth-first.

        Start at the root, and return None if not found.
        """

        to_visit = [self.root]

        while to_visit:
            node = to_visit.pop()

            if node.data == data:
                return node

            to_visit.extend(node.children)


def get_descendants(node, tracker=[], lvl=1):
    """Given a node, get all that node's children in a list. Assumes you're
    starting with a root node, making the first descendant level 1.

    For the following tree:

                       A
                     /   \
                    B     C
                   /  \     \
                  D    E     F
                        \
                         G

    Where A = lv 0, B/C = lv1, D/E/F = lv2, G = lv3, the following example
    shows the descendants. We take a depth first approach here, getting
    all descendants of B before getting descendants of C.

    >>> a = Node("A")
    >>> b = Node("B")
    >>> c = Node("C")
    >>> d = Node("D")
    >>> e = Node("E")
    >>> f = Node("F")
    >>> g = Node("G")
    >>> a.children = [b,c]
    >>> b.children = [d,e]
    >>> c.children = [f]
    >>> tree = Tree(a)
    >>> e.children=[g]
    >>> print(get_descendants(tree.root))
    [(<Node B>, 1), (<Node D>, 2), (<Node E>, 2), (<Node G>, 3), (<Node C>, 1), (<Node F>, 2)]

    """

    # Set list to return equal to list passed.
    descendants = tracker

    # For each child of the passed node, check whether that child is in the 
    # current descendants list. If not, append it, along with its tree level.
    # Then, call this function on that child, passing the current list.
    for child in node.children:
        if child not in descendants:
            descendants.append((child, lvl))

            # Recursion!!!!
            get_descendants(child, descendants, lvl+1)

    return descendants





    def breadth_first_search(self, data):
        """Return node object with this data, traversing the tree breadth-first.

        Start here (on this node), and return None if not found.

        Let's make a tree where we have two "B" nodes, but where one is far down an
        earlier branch and the other is higher-up in an earlier branch. Since this is
        a BFS, we should find the b2 node for "B"::

                       A
                     /   \
                    C     E
                   /       \
                  D        B2
                 /
                B1

            >>> a = Node("A")
            >>> b1 = Node("B")
            >>> b2 = Node("B")
            >>> c = Node("C")
            >>> d = Node("D")
            >>> e = Node("E")
            >>> a.children = [c, e]
            >>> c.children = [d]
            >>> d.children = [b1]
            >>> e.children = [b2]
            >>> tree = Tree(a)

            >>> tree.breadth_first_search("B") is b2
            True

            (Adding a new doctest to check that we return none for something that
            isn't in the tree, as requested.)

            >>> a = Node("A")
            >>> b1 = Node("B")
            >>> b2 = Node("B")
            >>> c = Node("C")
            >>> d = Node("D")
            >>> e = Node("E")
            >>> a.children = [c, e]
            >>> c.children = [d]
            >>> d.children = [b1]
            >>> e.children = [b2]
            >>> tree = Tree(a)

            >>> print(tree.breadth_first_search("F"))
            None

        """

        to_visit = [self.root]

        while to_visit:
            node = to_visit.pop(0)

            if node.data == data:
                return node

            to_visit.extend(node.children)

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

