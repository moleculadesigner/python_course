import re
import math

binary_operators = {
    '+' : (3, 'L', lambda a, b: b + a),
    '-' : (3, 'L', lambda a, b: b - a),
    '*' : (4, 'L', lambda a, b: b * a),
    '/' : (4, 'L', lambda a, b: b / a),
    '^' : (5, 'R', lambda a, b: b ** a)
    }

float_re = re.compile(r"^\d+?\.\d+?$")

def mk_tokens_list(expr):
    """
    Parses input expression and returns list of tokens to be processed via shunting yard algorythm.
    """
    parser = re.compile(r'[a-z_]+|[-+*\/\^]|[()]|\d+\.?\d*')
    return parser.findall(expr)

def shunting_yard(tokens):
    mask = ''
    stack = []
    postfix = []
    for token in tokens:
        if token.isdigit():
            postfix.append(int(token))
            mask += 'd '
        elif float_re.match(token):
            postfix.append(float(token))
            mask += 'f '
        elif token in binary_operators.keys():
            postfix.append(token)
            mask += 'o '
        elif token == '(' or token == ')':
            mask += 'b '
        else:
            mask += '? '
    print(mask)
    print(str(postfix))

e = "asd + 45 - 12.4^(12*4/56.01), ,"
print(e)
shunting_yard(mk_tokens_list(e))

