class Node():
    """
    A node/subtree in abstract synax tree.

    Fields:
    * `name` A node name.
    * `id` Unique number.
    * `leaf` **True** if there are no children nodes.
    * `expression` lambda expression if not a leaf.
    * `children` list of successor nodes.

    Methods:
    * `grow(node)` Add a `node` into the left unsetttled child node.
    * `render()` Return a value of tree (process all subtrees).
    * `strip()` Clear the rightest settled child node.
    """