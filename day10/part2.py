with open("input.txt") as f:
    lines = [list(line) for line in f.read().splitlines()]

m, n = len(lines), len(lines[0])
nexts = {"0": "1", "1": "2", "2": "3", "3": "4", "4": "5", "5": "6", "6": "7", "7": "8", "8": "9"}

def findScore(c, x, y):
    if c == "9":
        return 1
    nxt = nexts.get(lines[x][y])
    sc = 0
    # check up
    if x>0 and nxt == lines[x-1][y]:
        sc+=findScore(lines[x-1][y], x-1, y)
    # check right
    if y<n-1 and nxt == lines[x][y+1]:
        sc+=findScore(lines[x][y+1], x, y+1)
        
    # check down
    if x<m-1 and nxt == lines[x+1][y]:
        sc+=findScore(lines[x+1][y], x+1, y)
    
    # check left
    if y>0 and nxt == lines[x][y-1]:
        sc+=findScore(lines[x][y-1], x, y-1)
        
    return sc
        
score = 0
for i in range(m):
    for j in range(n):
        if lines[i][j]=="0":
            score+=findScore("0", i, j)
print(score)