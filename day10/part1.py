with open("input.txt") as f:
    lines = [list(line) for line in f.read().splitlines()]

m, n = len(lines), len(lines[0])
nexts = {"0": "1", "1": "2", "2": "3", "3": "4", "4": "5", "5": "6", "6": "7", "7": "8", "8": "9"}

def findScore(c, x, y, coords):
    if c == "9":
        coords.add((x, y))
        return
    
    nxt = nexts.get(lines[x][y])
    #check up
    if x>0 and nxt == lines[x-1][y]:
        findScore(lines[x-1][y], x-1, y, coords)
    # check right
    if y<n-1 and nxt == lines[x][y+1]:
        findScore(lines[x][y+1], x, y+1, coords)
        
    # check down
    if x<m-1 and nxt == lines[x+1][y]:
        findScore(lines[x+1][y], x+1, y, coords)
    
    # check left
    if y>0 and nxt == lines[x][y-1]:
        findScore(lines[x][y-1], x, y-1, coords)
        
score = 0
for i in range(m):
    for j in range(n):
        if lines[i][j]=="0":
            nineCoords = set()
            findScore("0", i, j, nineCoords)
            score+=len(nineCoords)
print(score)