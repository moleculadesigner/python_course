import re
import math
from node import *
from copy import deepcopy

operators = {
    '+' : (3, 'L', [lambda a, b: b + a, 2]),
    '-' : (3, 'L', [lambda a, b: b - a, 2]),
    '*' : (4, 'L', [lambda a, b: b * a, 2]),
    '/' : (4, 'L', [lambda a, b: b / a, 2]),
    '^' : (5, 'R', [lambda a, b: b ** a, 2])
    }

functions = {
    'sum'   : Node('sum', lambda a, b: b + a, 2)
}

float_re = re.compile(r"^\d+?\.\d+?$")

def mk_tokens_list(expr):
    """
    Parses input expression and returns list of tokens to be processed via shunting yard algorythm.
    """
    parser = re.compile(r'[a-z_]+|[-+*\/\^(),]|\d+\.?\d*')
    return parser.findall(expr)

def apply(op, q):
    for i in len(op.children):
        op.grow(q.pop())
    q.append(op)

def shunting_yard(tokens):
    mask = ''
    stack = []
    queue = []
    tree = Node('Expression', lambda x: x, 1)
    for token in tokens:
        if token.isdigit():
            queue.append(wrap(int(token)))
        elif float_re.match(token):
            queue.append(wrap(float(token)))

        elif token in functions.keys():
            stack.append(deepcopy(functions[token]))

        elif token == ',':
            while stack[-1].name != '(':
                apply(stack.pop(), queue)
                
        elif token in operators.keys():
            while stack[-1].name in operators and ((operators[token][1] == 'L' and operators[token][0] <= operators[stack[-1].name][0]) or (operators[token][1] == 'R' and operators[token][0] < operators[stack[-1].name][0])):
                apply(stack.pop(), queue)
            stack.append(Node(token, *operators[token][2]))

        elif token == '(':
            stack.append(Node(token))

        elif token == ')':
            while stack[-1].name != '(':
                apply(stack.pop(), queue)
            
        else:
            mask += '? '
    print(mask)
    print(str(queue))

e = "0.03 + 45 - 12.4^(12*4/56.01)"
print(e)
shunting_yard(mk_tokens_list(e))

