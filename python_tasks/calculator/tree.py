import random

tree = [
    None,
    [
        None,
        None
    ],
    [
        None,
        12,
        [
            None,
            2,
            None
        ],
        None
    ],
    [
        None
    ]
]

t1 = [
    None,
    [
        None,
        None,
        [
            None,
            None
        ]
    ]
]

t2 = [
    None,
    [
        None,
        None
    ]
]

def is_list(list):
    try:
        len(list)
    except TypeError:
        return False
    return True

def deeps(tree, lvl = ''):
    if not is_list(tree):
        return 0
    if not len(tree):
        return 0
    lvl += '.'
    for node in tree:
        print(lvl)
        deeps(node, lvl)
        

def assign(tree, leafs = [i for i in range(100)]):
    for i in range(len(tree) -1, -1, -1):
        if not is_list(tree[i]):
            if not tree[i]:
                tree[i] = leafs.pop()

        else:
            assign(tree[i], leafs)


def draw_tree(tree, lvl = 0):
    if not is_list(tree) or not len(tree):
        s = ''
        for i in range(lvl):
            s += '┊\t'
        return s +  str(tree) + '\n'
    lvl += 1
    s = ''
    for i in range(lvl-1):
        s += '┊\t'
    s += '╭ ' + random.choice(['+','-','*','/','^','sin']) + '\n'
    for node in tree:
        s += draw_tree(node, lvl)
    return s

     

assign(t1)
assign(t2)
means = [0, 0, 0, 1, 2, 3, 4, 5, 6, 7, t2, t1]
assign(tree, means)
print(draw_tree(tree))