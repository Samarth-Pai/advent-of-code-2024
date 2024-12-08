from collections import defaultdict
with open("input.txt") as f:
    lines = f.read().splitlines()
    
    
lineList = list(map(list, lines))
m, n = len(lines), len(lines[0])
antennas = defaultdict(list[tuple[int, int]])

def coordExists(i, j):
    return 0<=i<m and 0<=j<n
    

for i in range(m):
    for j in range(n):
        if lines[i][j] not in ["#", "."]:
            antennas[lines[i][j]].append((i, j))

for ant, coords in antennas.items():
    for coord in coords:
        lineList[coord[0]][coord[1]] = "#"
    for i in range(len(coords)):
        coord = coords[i]
        remainingCoords = coords[:i] + coords[i+1:]
        for c in remainingCoords:
            dx, dy = c[0] - coord[0], c[1] - coord[1]
            nextCoord = (c[0] + dx ,c[1] + dy)
            while coordExists(*nextCoord):
                lineList[nextCoord[0]][nextCoord[1]] = "#"
                nextCoord = (nextCoord[0]+ dx,nextCoord[1] + dy)
            
hashtags = sum(map(lambda x:x.count("#"), lineList))
print(hashtags)