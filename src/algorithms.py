import numpy as np

def N4(p, a, b):
    N = []
    if p[1] != 0: N.append((p[0], p[1]-1))
    if p[0] != 0: N.append((p[0]-1, p[1]))
    if p[1] != b-1: N.append((p[0], p[1]+1))
    if p[0] != a-1: N.append((p[0]+1, p[1]))
    return N

def N8(p, a, b):
    N = []
    if p[1] != 0: N.append((p[0], p[1]-1))
        if p[0] != 0: N.append((p[0]-1, p[1]-1))
        if p[0] != a-1: N.append((p[0]+1, p[1])-1)

    if p[0] != 0: N.append((p[0]-1, p[1]))
        if p[1] != 0: N.append((p[0]-1, p[1]-1))
        if p[1] != b-1: N.append((p[0]-1, p[1]+1))


    if p[1] != b-1: N.append((p[0], p[1]+1))
        if p[0] != 0: N.append((p[0]-1, p[1]+1))
        if p[0] != a-1: N.append((p[0]+1, p[1]+1))

    if p[0] != a-1: N.append((p[0]+1, p[1]))
        if p[1] != 0: N.append((p[0]+1, p[1]-1))
        if p[1] != b-1: N.append((p[0]+1, p[1]+1))
    return N

def WS(inp, Nx)