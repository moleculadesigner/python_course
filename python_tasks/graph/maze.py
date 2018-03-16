import numpy as np

def convert(smap:str):
    m = smap.split('\n')
    h = len(m)
    l = len(m[0])
    mz = np.zeros((h, l), dtype=np.int64)
    s, e = None, None

    for i, row in enumerate(m):
        if len(row) != l:
            raise ValueError("Maze map must be rectangular.")
        for j, tile in enumerate(row):
            if tile == '-':
                mz[i, j] = 1
            elif tile == 'P':
                if s is None:
                    mz[i, j] = 1
                    s = (i, j)
                else:
                    raise ValueError("Too much start points.")
            elif tile == 'T':
                if e is None:
                    mz[i, j] = 1
                    e = (i, j)
                else:
                    raise ValueError("Too much end points.")
    if s is None or e is None:
        raise ValueError("There is no start/end point.")

    return mz, s, e

with open("find_path.ai", 'r') as path:
    smap = path.read().strip()

print(convert(smap))