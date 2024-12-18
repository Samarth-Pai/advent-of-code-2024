import heapq
with open("input.txt") as f:
    lines = f.read().splitlines()
    
track = [list(s) for s in lines]
m, n = len(track), len(track[0])

x, y = m-2, 1
d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
def findPath(coord):
    # time.sleep(0.6)
    # (turns, length, x, y, direction)
    visited = set()
    pq = []
    for en, (dx, dy) in enumerate(d):
        nx, ny = coord[0] + dx, coord[1] + dy
        if track[nx][ny]!="#":
            heapq.heappush(pq, (en!=1, 1, nx, ny, en))
    
    while pq:
        t, l, x, y, diri = heapq.heappop(pq)
        if track[x][y] == "E":
            return t*1000 + l

        if (x, y, diri) in visited:
            continue
        visited.add((x, y, diri))
        
        for en, (dx, dy) in enumerate(d):
            nx, ny = x + dx, y + dy
            if track[nx][ny]!="#":
                newTurn = t + (en!=diri)
                heapq.heappush(pq, (newTurn, l + 1, nx, ny, en))
    return -1
    
            
        
initCoord = (x, y)
res = findPath(initCoord)
print(res)