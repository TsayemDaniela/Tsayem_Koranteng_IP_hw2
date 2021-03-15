import numpy as np

# Function for 4 Pixel Neighbourhood
def N4(p, a, b):
    N = []
    if p[1] != 0: N.append((p[0], p[1]-1))
    if p[0] != 0: N.append((p[0]-1, p[1]))
    if p[1] != b-1: N.append((p[0], p[1]+1))
    if p[0] != a-1: N.append((p[0]+1, p[1]))
    return N

# Function for 8 Pixel Neighbourhood
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

def WS(inp, Nx):
    msk = -2 # Initial Threshold
    ws = 0 # Pixel Value in Watersheds
    val = -1 # Initial inp value
    inque = -3 # value assigned to pixels put into the queue
    current_label = 0
    flag = False
    H, W = inp.shape
    out = np.full((H,W), val, np.int32)
    fifo = []
    # Sorting GrayValues
    pxl = list(set(inp.flatten()))
    pxl.sort()
    for h in pxl:
        hid = []
        # All Occurences of h
        for x in range(H):
            for y in range(W):
                if inp[x,y] == h:
                    hid.append((x,y))
        # Mask all h
        for idx in hid:
            out[idx[0]][idx[1]] = msk
            # Check Neighbourhood for WaterShed
            nid = Nx(idx, H, W)
            for n in nid:
                if out[n[0]][n[1]] == ws or out[n[0]][n[1]] > 0:
                    out[idx[0]][idx[1]] = inque
                    fifo.append(idx)
                    break
        # Validating Watershed
        while len(fifo) != 0:
            p = fifo.pop(0)
            # Check if Neighbourhood in Labelled Basin
            nid = Nx(p, H, W)
            for n in nid:
                if out[n[0]][n[1]] > 0:
                    if out[p[0]][p[1]] == inque or (out[p[0]][p[1]] == ws and flag == True):
                        out[p[0]][p[1]] = out[n[0]][n[1]]
                    elif out[p[0]][p[1]] > 0 and out[p[0]][p[1]] != out[n[0]][n[1]]:
                        out[p[0]][p[1]] = ws
                        flag = False
                elif out[n[0]][n[1]] == ws:
                    if out[p[0]][p[1]] == inque:
                        out[p[0]][p[1]] = ws
                        flag = True
                elif out[n[0]][n[1]] == msk:
                    out[n[0]][n[1]] = inque
                    fifo.append((n[0], n[1]))
        # Check New Minima
        for idx in hid:
            if out[idx[0]][idx[1]] == msk:
                current_label += 1
                fifo.append(idx)
                out[idx[0]][idx[1]] = current_label
                while len(fifo) != 0:
                    p = fifo.pop(0)
                    nid = Nx(p, H, W)
                    for n in nid:
                        if out[n[0]][n[1]] == msk:
                            fifo.append(n)
                            out[n[0]][n[1]] = current_label
    return out