import re
import math
from node import *

operators = {
    '+'     : (3, 'L', [lambda a, b: a +  b, 2]),
    '-'     : (3, 'L', [lambda a, b: a -  b, 2]),
    '*'     : (4, 'L', [lambda a, b: a *  b, 2]),
    '/'     : (4, 'L', [lambda a, b: a /  b, 2]),
    '^'     : (5, 'R', [lambda a, b: a ** b, 2])
    }

functions = {
    'sum'   : Node('sum', lambda a, b, c: a + b + c, 3)
}

variables = {
    'pi'    : 3.1415926,
    'e'     : 2.7182818
}

float_re = re.compile(r"^\d+?\.\d+?$")

def parse(expr):
    """
    Parses input expression and returns list of tokens to be processed via shunting yard algorythm.
    """
    parser = re.compile(r'[a-z_]+|[-+*\/\^(),]|\d+\.?\d*')
    return parser.findall(expr)

def apply(op, q):
    """
    Takes number of arguments from queue (`q`) and appends them to operator (`op`) tree.

    Example:
    * `op` - tree with function `sum(a, b, c)` and 3 arguments
    * `q = [1, 2, 3, 4]` where numbers are wrapped into the **Node** class
    * after `apply(op, q)` -> `q = [1, sum(2, 3, 4)]`
    """
    args = []
    for i in range(op.freenodes()):
        try:
            args.append(q.pop())
        except IndexError:
            print("Not enough arguments in function {}.".format(op.name))
    while args:
        op.grow(args.pop())
    q.append(op)


def makeAST(tokens):
    """
    Takes a list of infix expression tokens and returns an [Abstrac Syntax Tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree) of this expression using [Shunting-yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm).
    """
    stack = []
    queue = []
    tree = Node('Expression', lambda x: x, 1)
    for token in tokens:
        #print("Token: {}".format(token))
        # Digits go directly to queue
        if token.isdigit():
            queue.append(wrap(int(token)))
        elif float_re.match(token):
            queue.append(wrap(float(token)))

        # Variables are handled as numbers
        elif token in variables.keys():
            queue.append(wrap(variables[token]))

        # Functions go to stack
        elif token in functions.keys():
            stack.append(deepcopy(functions[token]))

        # Function args separator
        elif token == ',':
            while stack and stack[-1].name != '(':
                apply(stack.pop(), queue)
            if not stack:
                print("Shunting yard: syntax error — missing '(' or ','.")
                raise SyntaxError           
        
        # Operators priority handling
        elif token in operators.keys():
            while stack and stack[-1].name in operators and((operators[token][1] == 'L' and operators[token][0] <= operators[stack[-1].name][0]) or (operators[token][1] == 'R' and operators[token][0] < operators[stack[-1].name][0])):
                apply(stack.pop(), queue)
            stack.append(Node(token, *operators[token][2]))

        elif token == '(':            
            stack.append(Node(token))

        elif token == ')':
            while stack and stack[-1].name != '(':
                apply(stack.pop(), queue)
            if not stack:
                print("Shunting yard: syntax error — missing '('.")
                raise SyntaxError
            elif stack[-1].name == '(':
                stack.pop()
                if stack and stack[-1].name in functions.keys():
                    apply(stack.pop(), queue)
            else:
                print("Shunting yard: unknown syntax error. Recheck the expression:\n> {}".format(' '.join(tokens)))
                raise SyntaxError            
            
        else:
            print("Unknown operation or invalid number.")
            raise SyntaxError
        # End of tokens

    # Utilizing op stack
    while stack:
        if stack[-1].name == '(':
            print("Shunting yard: missing ')'.")
            raise SyntaxError
        else:
            apply(stack.pop(), queue)

    if len(queue) == 1:
        #print(queue[0].show())
        return queue[0]          
    else:
        print("Failed to render syntax tree: invalid number of arguments")
        for node in queue:
            print("{}:\n{}".format(node.name, node.show()))

    
    print(str(queue))

expr = "sum(1,2,3) * 0.03 + 45 - e^(12*4/56.01)"
print(expr)
ast = makeAST(parse(expr))
print(ast.show())
print(ast.render())

