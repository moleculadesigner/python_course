help = """    
    Arithmetical expressions evaluator help
    
    Just print arithmetical expression to evaluate it.

    You also can assign an expression or number to the variable
    with let operator:
    let [var_name] [expression or number]
    > let kappa 2.148
    > let k_factor 1/kappa^5

    The same thing with function keyword:
    function [func_name](par_one, par_two, ...) [expression]
    > function avrg(a, b) a/b + b/a
    > function field(a, b) avrg(a, b) * e^k_factor

\x1b[31mN.B.
    Variable and function names must consist only
    of a-z and _ characters.
\x1b[0m

    To view functions and variables print reveal and you will get
    something like this:

    > reveal
    Functions:
    id(x)
    avrg(a, b) =  a/b+b/a

    Variables:          
    pi      3.1415926
    e       2.7182818

    As the evaluator works by means of syntax tree rendering, you can
    draw it for any function or expression. But be careful: incomplete
    expression will render into a wrong tree.
    > tree field
    > tree 2 + avrg(1,5)

    To exit type one of this keywords:
    exit
    quit
    close

    Author: Dan Iakovlev
            \x1b[34mmoleculadesigner@gmail.com\x1b[0m
    License: WTFPL
"""

if __name__ == '__main__':
    print(help)