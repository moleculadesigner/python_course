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
    'id'    : (Node('id', lambda x: x, 1, None, 'id(a)'))}

variables = {
    'pi'    : 3.1415926,
    'e'     : 2.7182818}

float_re = re.compile(r"^\d+?\.\d+?$")
varname_re = re.compile(r"^[a-z_]+?$")
parse_re = re.compile(r'[a-z_]+|[-+*\/\^(),]|\d+\.?\d*')

# Literals
# borders: │┊╭─╮╰╯
greeting = (
    "╭---------------------------------------------------╮\n"+
    "┊ Arithmetical expressions evaluator                ┊\n"+
    "┊ Type help for further instructions                ┊\n"+
    "┊ Author: Dan Iakovlev (moleculadesigner@gmail.com) ┊\n"+
    "┊ 2017                                              ┊\n"+
    "╰---------------------------------------------------╯\n")

stop = [
    'exit',
    'quit',
    'close']


def show_help():
    with open('help') as hfile:
        print(hfile.read())


def parse(expr):
    """
    Parses input expression and returns list of tokens to be processed via shunting yard algorythm.
    """
    return parse_re.findall(expr)


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


def make_AST(tokens, params = []):
    """
    Takes a list of infix expression tokens and returns an [Abstrac Syntax Tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree) of this expression using [Shunting-yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm).
    """
    stack = []
    queue = []

    parameters = {}
    for p in params:
        if p in (list(variables.keys()) + list(functions.keys()) + list(parameters.keys())):
            print("Function parameter ({}) may not be a variable or function name.".format(p))
            raise SyntaxError
        else:
            n = Node(p, lambda x: x, 1)
            n.grow(wrap('♦'))
            parameters[p.split('.')[0]] = [
                n, # a parameter node with function Id (\x. x) and a dummy leaf. 
                0 # How many times the parameter was used
            ]
            

    for token in tokens:
        # Numcers go directly to the queue
        if token.isdigit():
            queue.append(wrap(int(token)))
        elif float_re.match(token):
            queue.append(wrap(float(token)))

        # Variables are handled as numbers
        elif token in variables.keys():
            v = wrap(variables[token])
            v.fname = "({})".format(token)
            queue.append(v)

        # Function parameters
        elif token in parameters.keys():
            if parameters[token][1]:
                queue.append(fakenode(parameters[token][0]))
            else:
                queue.append(parameters[token][0])
            parameters[token][1] += 1

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
                if stack and stack[-1].fname.split("(")[0] in functions.keys():
                    apply(stack.pop(), queue)
            else:
                print("Shunting yard: unknown syntax error. Recheck the expression:\n> {}".format(' '.join(tokens)))
                raise SyntaxError            
            
        else:
            print("Unknown operation or invalid number.")
            raise SyntaxError
        
        #print("Stack: {}\nQueue: {}\n".format(' '.join([s.name for s in stack]), ' '.join([q.name for q in queue])))
        
        # End of tokens

    # Utilizing op stack
    while stack:
        if stack[-1].name == '(':
            print("Shunting yard: missing ')'.")
            raise SyntaxError
        else:
            apply(stack.pop(), queue)
        #print("Stack: {}\nQueue: {}\n".format(' '.join([s.name for s in stack]), ' '.join([q.name for q in queue])))

    # Removing dummy leafs from parameters
    if params:
        for p in parameters.keys():
            parameters[p][0].strip()

    if len(queue) == 1:
        return queue[0]          
    else:
        print("Failed to render syntax tree: invalid number of arguments")
        for node in queue:
            print("{}:\n{}".format(node.name, node.show()))


def add_variable(varname: str, tokens: list):
    if not varname_re.match(varname):
        print("Invalid variable name: {}".format(varname))
        raise SyntaxError
    elif varname in variables.keys():
        print("Variable {} already exists.".format(varname))
        raise ValueError
    else:
        variables[varname] = make_AST(tokens).render()


def add_function(tokens):
    funcname = tokens[0]
    if not varname_re.match(funcname):
        print("Invalid function name: {}".format(funcname))
        raise SyntaxError
    params = []
    if tokens[1] == '(':
        for c in range(2, len(tokens)):
            if tokens[c] == ')':
                close = c + 1
                break
            elif tokens[c] == ',':
                continue
            else:
                params.append('{}.{}'.format(tokens[c], funcname))
    else:
        print("Invalid function definition: {}".format(' '.join(tokens)))
    ast = make_AST(tokens[close:], params)
    ast.fname = "{}({}) = {}".format(funcname, ', '.join(map(lambda x: x.split('.')[0], params)), "".join(tokens[close:]))
    functions[funcname] = ast




def calculator():
    print(greeting)
    while True:
        raw = input("math > ")
        commands = parse(raw)
        if not commands:
            continue
        elif commands[0] in stop:
            return

        elif commands[0] == 'let': # Assign a new variable
            try:
                add_variable(commands[1], commands[2:])
            except Exception:
                continue 
            print("Remembered {} = {}".format(commands[1], variables[commands[1]]))

        elif commands[0] == 'function': # Assign a new function
            try:
                add_function(commands[1:])
            except Exception:
                continue
            print("Function {} is saved.".format(functions[commands[1]].fname))

        elif commands[0] == 'tree': # Draw syntax tree for following expression
            if commands[1:]:
                try:
                    ast = make_AST(commands[1:])
                except Exception:
                    continue
                print(ast.show())
            else:
                print("Nothing to draw")

        elif commands[0] == 'help': # Show help
            show_help()
               
        elif commands[0] == 'reveal': # Show list of functions and variables
            print("Functions:")
            for f in functions.values():
                print(f.fname)
            print("\nVariables:")
            for v in variables.items():
                print("{}\t{}".format(v[0], v[1]))

        else:
            try:
                ast = make_AST(commands)
                result = ast.render()
            except Exception:
                print("Error")
                continue
            print(result)


def demo():
    add_variable('g', ['9.8'])
    add_function(parse('del(a, b, c) a*c + b'))
    print(functions['del'].show())
    expr = "del(2,3, 5) * 0.03 + 45 - e^(12*4/56.01)"
    print(expr)
    ast = make_AST(parse(expr))
    print(ast.show())
    print(ast.render())

if __name__ == '__main__':
    calculator()

