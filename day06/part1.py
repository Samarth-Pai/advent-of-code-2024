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

nextDirs = {"^":">", ">": "v", "v": "<", "<": "^"}
def onCorner():
    return x==0 or x==m-1 or y==0 or y==n-1

places = set()
places.add((x,y))
while not onCorner():
    if currDir=="^":
        if lines[x-1][y]=="#":
            currDir = nextDirs[currDir]
            continue
        x-=1
    elif currDir==">":
        if lines[x][y+1]=="#":
            currDir = nextDirs[currDir]
            continue
        y+=1
    elif currDir=="v":
        if lines[x+1][y]=="#":
            currDir = nextDirs[currDir]
            continue
        x+=1
    else:
        if lines[x][y-1]=="#":
            currDir = nextDirs[currDir]
            continue
        y-=1
    places.add((x, y))
    
print(len(places))