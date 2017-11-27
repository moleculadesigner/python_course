from functools import partial
from copy import deepcopy, copy
from inspect import signature

#def partial(func, arg):
#    def curry(*args):
#        return func(arg, *args)
#    return curry

leaf = 'leaf'
link = '○ <<'

class Node():
    """
    A node/subtree in abstract synax tree.
    
    **Fields**:
    * `name` An operator name or 'leaf' if there are no child nodes.
    * `expression` the leaf value or lambda expression if not a leaf.
    * `children` a list of child nodes.

    **Methods**:
    * `grow(node)` Add a `node` into the left unsetttled child node.
    * `render()` Returns a value of tree (process all subtrees).
    * `strip()` Returns the rightest settled child node and clear it.
    * `check()` Iteratively matches number of operands and number of children and returns **True** if correct.
    * `show()` Returns string containing a schematic view of the node subtree.
    """
    name = str()
    expression = 0
    children = []
    parent = None

    def __init__(self, name = leaf, expression = 0, child_num = 0, parent = None):
        """
        Creates a new leaf or node with unsettled children.
        """
        self.name = name
        self.expression = expression
        self.children = []
        for i in range(child_num):
            self.children.append(None)
        self.parent = parent
        
    def render(self):
        """Returns a value of tree (process all subtrees)."""
        if self.name == leaf:
            return self.expression
        result = self.expression
        
        for node in self.children:
            if node != None:
                result = partial(result, node.render())
            else:
                print("Render error: lack of arguments in function {}{}.".format(self.name, str(signature(result))))
                raise ValueError
            
        #try:
        #    result()
        #except TypeError as ArgLack:
        #    #print("Node.render(): syntax tree is incomplete, reterning a partially applied function instead of value.\nNode.render(): " + str(ArgLack))
        #    print("return: func" + str(signature(result)))
        #    return result
        return result()

    def grow(self, node):
        """Add a `node` into the left unsetttled child node."""
        if self.name == leaf or self.name == link:
            return False
        for i in range(len(self.children)):
            if self.children[i] == None:
                if not node.parent:
                    self.children[i] = node
                    node.parent = self
                    return True
            else:
                self.children[i].grow(node)

    def show(self, level = 0):
        """Returns string containing a schematic view of the tree."""
        s = ''
        if self.name == leaf:
            for i in range(level):
                s += '┊\t'
            return s + str(self.expression) + '\n'
        #elif self.name == '○ <<':
        #    for i in range(level):
        #        s += '┊\t'
        #    return s + '○ << ' + self.children[0].name + '\n'
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
                s += '○\n' #∘○◌
        return s  

def wrap(number):
    """Just an alias to `Node('leaf', number)` method, creating a leaf node."""
    return Node(leaf, number)

def fakenode(node):
    """Creates a new node with a link to `node`. Use carefully: high risk of endless recursion."""
    fl = Node(link, lambda x: x, 1)
    fl.children[0] = node
    return fl

def demo():
    print("Abstract syntax tree class demo:")
    print("1. Creating a '+' operator node n:\n>>> n = Node('+', lambda a, b: b + a, 2)")
    n = Node('+', lambda a, b: b + a, 2)
    print("\n2. Making a new node k with the same operator:\n>>> k = deepcopy(n)\n>>> l = deepcopy(n)")
    k = deepcopy(n)
    l = deepcopy(n)
    print("\n3. Tuning it:\n>>> k.name = '•'\n>>> l.name = 'sum'\n>>> k.expression = lambda a, b: b * a")
    k.name = '•'
    l.name = 'sum'
    k.expression = lambda a, b: b * a
    print("\n4. Also we need some arguments (leaf nodes):\n>>> m = Node('leaf', 3) (m = 3)\n>>> o = Node('leaf', 5) (o = 5)\n>>> q = wrap(3) (q = 3): shorter way")
    m = Node(leaf, 3)
    o = wrap(5)
    q = wrap(3)
    print("\n5. Sometimes we need to draw a tree:\n>>> print(k.show())")
    print(k.show())
    print("\n6. Setting up a tree:\n>>> n.grow(m)")
    n.grow(m)
    print(n.show())
    print(">>> n.grow(o)")
    n.grow(o)
    print(n.show())
    print("A tree may be inserted into another tree:\n>>> k.grow(n)\n>>> k.grow(l)")
    k.grow(n)
    k.grow(l)
    print(k.show())

    
    print("7. This tree represents a function of 2 arguments, so trying to render it will raise a ValueError:\n>>> k.render()")
    try:
        k.render()
    except ValueError:
        print('We cannot render functions yet, only complete expressions.\n')
    print("8. Finalizing and render tree:\n>>> l.grow(fakenode(n)) — link to node n")
    print("And adding an absolutely new leaf:\n>>> k.grow(Node('leaf', 1.25))")
    l.grow(fakenode(n))
    k.grow(Node('leaf', 1.25))
    print(k.show())
    print("The tree could be easily converted into postfix notation:\n3 5 + 1.25 + 3 5 + * = {}".format(k.render()))

if __name__ == '__main__':
    demo()

