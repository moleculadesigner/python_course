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
    'id'    : Node('id', lambda x: x, 1, None, 'id(a)')
}

variables = {
    'pi'    : 3.1415926,
    'e'     : 2.7182818
}

float_re = re.compile(r"^\d+?\.\d+?$")
varname_re = re.compile(r"^[a-z_]+?$")
parse_re = re.compile(r'[a-z_]+|[-+*\/\^(),]|\d+\.?\d*')

greeting = (
    "*****************************************************\n"+
    "* Arithmetical expressions evaluator                *\n"+
    "* Author: Dan Iakovlev (moleculadesigner@gmail.com) *\n"+
    "* 2017                                              *\n"+
    "*****************************************************\n")



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
            parameters[p] = [
                n, # a parameter node with function Id (\x. x) and a dummy leaf. 
                0 # How many times the parameter was used
            ]
            

    for token in tokens:
        #print("Token: {}".format(token))
        # Digits go directly to queue
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

    if params:
        for p in parameters.keys():
            parameters[p][0].strip()

    if len(queue) == 1:
        #print(queue[0].show())
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


def add_function(funcname, tokens, params):
    ast = make_AST(tokens, params)
    ast.fname = "{}({})".format(funcname, ", ".join(params))
    functions[funcname] = ast


def show_help():
    print("Help")

def calculator():
    while True:
        print(greeting)
        raw = input("math > ")
        commands = parse(raw)
        if not commands:
            continue
        elif commands[0] == 'exit':
            return

        elif commands[0] == 'let':
            try:
                add_variable(commands[1], commands[2:])
            except Exception:
                continue 
            print("Remembered {} = {}".format(commands[1], variables[commands[1]]))

        elif commands[0] == 'function':
            funcname = commands[1]
            params = []
            if commands[2] == '(':
                for c in range(3, len(commands)):
                    if commands[c] == ')':
                        close = c + 1
                        break
                    elif commands[c] == ',':
                        continue
                    else:
                        params.append(commands[c])
            else:
                print("Invalid function definition.")
            try:
                add_function(funcname, commands[close:], params)
            except Exception:
                continue
            print("Function {}({}) = {} is saved.".format(funcname, ", ".join(params), "".join(commands[close:])))

        elif commands[0] == 'tree':
            try:
               ast = make_AST(commands[1:])
            except Exception:
                continue
            print(ast.show())

        elif commands[0] == 'help':
            show_help()
               
        elif commands[0] == 'reveal':
            print("Functions:")
            for f in functions.items():
                print("{}\t{}".format(f[0], f[1].fname))
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
    add_function('del', parse('(a + c)/b'), ['a', 'b', 'c'])
    print(functions['del'].show())
    expr = "del(2,3, 5) * 0.03 + 45 - e^(12*4/56.01)"
    print(expr)
    ast = make_AST(parse(expr))
    print(ast.show())
    print(ast.render())

if __name__ == '__main__':
    calculator()

