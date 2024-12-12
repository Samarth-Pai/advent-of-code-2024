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
    price = 0
    for x, y in params:
        price+=(x-1, y) not in params
        price+=(x, y+1) not in params
        price+=(x+1, y) not in params
        price+=(x, y-1) not in params
    return price
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