with open('input.txt') as f:
    lines = f.read()
    
    
warehouse, movements = map(str.splitlines, lines.split("\n\n"))
warehouse = [list(s) for s in warehouse]
movements = "".join(movements)

x, y = -1, -1
for i, s in enumerate(warehouse):
    for j, c in enumerate(s):
        if c == "@":
            x, y = i, j
            break

def makeMovement(m: str, x, y):
    if m=="^":
        if warehouse[x-1][y]==".":
            warehouse[x-1][y], warehouse[x][y] = warehouse[x][y] , warehouse[x-1][y]
            return x-1, y
        elif warehouse[x-1][y] == "O":
            nx, ny = makeMovement(m, x-1, y)
            if (nx, ny) == (x-2, y):
                warehouse[x-1][y], warehouse[x][y] = warehouse[x][y] , warehouse[x-1][y]
                return x-1, y
    elif m=="<":
        if warehouse[x][y-1] == ".":
            warehouse[x][y-1], warehouse[x][y] = warehouse[x][y], warehouse[x][y-1]
            return x, y-1
        elif warehouse[x][y-1] == "O":
            nx, ny = makeMovement(m, x, y-1)
            if (nx, ny) == (x, y-2):
                warehouse[x][y-1], warehouse[x][y] = warehouse[x][y], warehouse[x][y-1]
                return x, y-1
    elif m=="v":
        if warehouse[x+1][y]==".":
            warehouse[x+1][y], warehouse[x][y] = warehouse[x][y] , warehouse[x+1][y]
            return x+1, y
        elif warehouse[x+1][y] == "O":
            nx, ny = makeMovement(m, x+1, y)
            if (nx, ny) == (x+2, y):
                warehouse[x+1][y], warehouse[x][y] = warehouse[x][y] , warehouse[x+1][y]
                return x+1, y
    else:
        if warehouse[x][y+1] == ".":
            warehouse[x][y+1], warehouse[x][y] = warehouse[x][y], warehouse[x][y+1]
            return x, y+1
        elif warehouse[x][y+1] == "O":
            nx, ny = makeMovement(m, x, y+1)
            if (nx, ny) == (x, y+2):
                warehouse[x][y+1], warehouse[x][y] = warehouse[x][y], warehouse[x][y+1]
                return x, y+1
    return x, y
        
        
def sumOfGps():
    summ = 0
    for i, s in enumerate(warehouse):
        for j, c in enumerate(s):
            if c=="O":
                summ+=100*i + j
    return summ

for m in movements:
    x, y = makeMovement(m, x, y)
    # print()
    # print(m)
    # print(*warehouse, sep="\n")
    # time.sleep(1)
    
ans = sumOfGps()
print(ans)