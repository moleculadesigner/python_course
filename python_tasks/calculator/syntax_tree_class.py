from functools import partial
from copy import deepcopy, copy

class Node():
    """
    A node/subtree in abstract synax tree.

    Fields:
    * `name` An operator name or 'leaf' if there are no child nodes.
    * `expression` the leaf value or lambda expression if not a leaf.
    * `children` a list of child nodes.

    Methods:
    * `grow(node)` Add a `node` into the left unsetttled child node.
    * `render()` Return a value of tree (process all subtrees).
    * `strip()` Return the rightest settled child node and clear it.
    * `check()` Matches number of operands and number of children and returns **True** if correct.
    * `show()` Returns string containing a schematic view of the node subtree.
    """
    name = str()
    expression = 0
    children = []

    def __init__(self, name = 'leaf', expression = 0, child_num = 0):
        """
        Creates a new leaf or node with unsettled children.
        """
        self.name = name
        self.expression = expression
        self.children = []
        for i in range(child_num):
            self.children.append(None)
        
    def render(self):
        if self.name == 'leaf':
            return self.expression
        result = self.expression
        for node in self.children:
            result = partial(result, node.render())
        return result()

    def grow(self, node):
        #print(str(id(self)) + ":\n" + self.show())
        if self.name == 'leaf' or not len(self.children):
            return False
        for i in range(len(self.children)):
            if self.children[i] == None:
                self.children[i] = node
                return True
            else:
                self.children[i].grow(node)

    def show(self, level = 0):
        s = ''
        if self.name == 'leaf':
            for i in range(level):
                s += '┊\t'
            return s + str(self.expression) + '\n'
        for i in range(level):
            s += '┊\t'
        s += '╭ ' + self.name + '\n'
        level += 1
        for child in self.children:
            if child:
                s += child.show(level)
            else:
                for i in range(level):
                    s += '┊\t'
                s += '○\n'
        return s

        
    

def main():
    print("Abstract syntax tree class demo:")
    print("1. Creating a '+' operator:\n>>> n = Node('+', lambda a, b: b + a, 2)")
    n = Node('+', lambda a, b: b + a, 2)
    k = deepcopy(n)
    m = Node('leaf', 1)
    o = Node('leaf', 5)
    q = Node('leaf', 3)
    print(k.show())
    n.grow(m)
    n.grow(o)
    k.grow(n)
    print(k.show())
    k.grow(q)

    print(k.show())
     



if __name__ == '__main__':
    main()