from collections import defaultdict
with open("input.txt") as f:
    lines = f.read().splitlines()
    
    
lineList = list(map(list, lines))
m, n = len(lines), len(lines[0])
antennas = defaultdict(list[tuple[int, int]])

def coordExists(i, j):
    return i>=0 and i<m and j>=0 and j<n and lineList[i][j]!="#"
    

for i in range(m):
    for j in range(n):
        if lines[i][j] not in ["#", "."]:
            antennas[lines[i][j]].append((i, j))

for ant, coords in antennas.items():
    for i in range(len(coords)):
        coord = coords[i]
        remainingCoords = coords[:i] + coords[i+1:]
        for c in remainingCoords:
            nextCoord = (c[0]+(c[0] - coord[0]),c[1] + (c[1] - coord[1]))
            if coordExists(*nextCoord):
                lineList[nextCoord[0]][nextCoord[1]] = "#"

hashtags = sum(map(lambda x:x.count("#"), lineList))
print(hashtags)