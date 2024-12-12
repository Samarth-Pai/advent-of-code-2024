import time
with open("input.txt") as f:
    lines = f.read().splitlines()

visited = set()
m, n = len(lines), len(lines[0])

def findParams(c, x, y, params):
    visited.add((x, y))
    params.add((x, y))
    if x>0 and lines[x-1][y] == c and (x-1, y) not in params:
        findParams(c, x-1, y, params)
    if y<n-1 and lines[x][y+1] == c and (x, y+1) not in params:
        findParams(c, x, y+1, params)
    if x<m-1 and lines[x+1][y] == c and (x+1, y) not in params:
        findParams(c, x+1, y, params)
    if y>0 and lines[x][y-1] == c and (x, y-1) not in params:
        findParams(c, x, y-1, params)

def findArea(params):
    borders = set()
    crossBorders = set()
    finalCrossBorders = set()
    for x, y in params:
        nw = x>0 and y>0 and lines[x-1][y-1] == lines[x][y]
        nn = x>0 and lines[x-1][y] == lines[x][y]
        ne = x>0 and y<n-1 and lines[x-1][y+1] == lines[x][y]
        e = y<n-1 and lines[x][y+1] == lines[x][y]
        se = x<m-1 and y<n-1 and lines[x+1][y+1] == lines[x][y]
        s = x<m-1 and lines[x+1][y] == lines[x][y]
        sw = x<m-1 and y>0 and lines[x+1][y-1] == lines[x][y]
        w = y>0 and lines[x][y-1] == lines[x][y]
        if (sm:=(w+nw+nn)) in [0, 2]:
            borders.add((x, y))
        elif sm==1 and x>0 and y>0 and lines[x-1][y-1] == lines[x][y]:
            borders.add((x, y))
            if (x, y) in crossBorders:
                finalCrossBorders.add((x, y))
            else:
                crossBorders.add((x, y))
            
        if (sm:=(nn+ne+e)) in [0, 2]:
            borders.add((x, y+1))
        elif sm==1 and x>0 and y<n-1 and lines[x-1][y+1] == lines[x][y]:
            borders.add((x, y+1))
            if (x, y+1) in crossBorders:
                finalCrossBorders.add((x, y+1))
            else:
                crossBorders.add((x, y+1))
            
        if (sm:=(e+se+s) )in [0, 2]:
            borders.add((x+1, y+1))
        elif sm==1 and x<m-1 and y<n-1 and lines[x+1][y+1] == lines[x][y]:
            borders.add((x+1, y+1))
            if (x+1, y+1) in crossBorders:
                finalCrossBorders.add((x+1, y+1))
            else:
                crossBorders.add((x+1, y+1))
            
        if (sm:=(s+sw+w) )in [0, 2]:
            borders.add((x+1, y))
        elif sm==1 and x<m-1 and y>0 and lines[x+1][y-1] == lines[x][y]:
            borders.add((x+1, y))
            if (x+1, y) in crossBorders:
                finalCrossBorders.add((x+1, y))
            else:
                crossBorders.add((x+1, y))
            
    return len(borders) + len(finalCrossBorders)

totalPrice = 0
for i in range(m):
    for j in range(n):
        if (i, j) not in visited:
            params = set()
            findParams(lines[i][j], i, j, params)
            area = findArea(params)
            p = len(params)
            totalPrice+=p*area
print(totalPrice)