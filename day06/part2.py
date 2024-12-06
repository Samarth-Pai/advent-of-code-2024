with open("input.txt") as f:
    lines = f.read().splitlines()
    
m, n = len(lines), len(lines[0])
x, y = 0, 0
currDir = ""
for i in range(m):
    for j in range(n):
        if lines[i][j] in "^>v<":
            x, y = i, j
            currDir = lines[i][j]
initX, initY = x, y
initDir = currDir

nextDirs = {"^":">", ">": "v", "v": "<", "<": "^"}
def onCorner(xx = x, yy = y):
    return xx==0 or xx==m-1 or yy==0 or yy==n-1

places = set()
places.add((x,y, currDir))
def isInfiniteLoop(x, y):
    obs = (x, y)
    currDir = initDir
    i, j = initX, initY
    corners = set()
    while not onCorner(i, j):
        if currDir=="^":
            if lines[i-1][j]=="#" or (i-1, j) == obs:
                currDir = nextDirs[currDir]
                if (i-1, j, currDir) in corners:
                    return True
                corners.add((i-1, j, currDir))
                continue
            i-=1
        elif currDir==">":
            if lines[i][j+1]=="#" or (i, j+1) == obs:
                currDir = nextDirs[currDir]
                if (i, j+1, currDir) in corners:
                    return True
                corners.add((i, j+1, currDir))
                continue
            j+=1
        elif currDir=="v":
            if lines[i+1][j]=="#" or (i+1, j) == obs:
                currDir = nextDirs[currDir]
                if (i+1, j, currDir) in corners:
                    return True
                corners.add((i+1, j, currDir))
                continue
            i+=1
        else:
            if lines[i][j-1]=="#" or (i, j-1) == obs:
                currDir = nextDirs[currDir]
                if (i, j-1, currDir) in corners:
                    return True
                corners.add((i, j-1, currDir))
                continue
            j-=1
    return False
        
totalLoops = 0
for i in range(m):
    for j in range(n):
        if (i, j)!=(initX, initY) and lines[i][j]==".":
            totalLoops+=isInfiniteLoop(i, j)
    
print(totalLoops)