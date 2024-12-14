import re
from copy import deepcopy
with open("input.txt") as f:
    lines = f.read().splitlines()
    
# m, n = 7, 11 for test
m, n = 103, 101
robots = [[[] for j in range(n)] for i in range(m)]
def moveRobots(robots):
    robotCopy = deepcopy(robots)
    for i in range(m):
        for j in range(n):
            for x, y in robots[i][j]:
                robotCopy[i][j].remove((x, y))
                robotCopy[(i+y)%m][(j+x)%n].append((x,y))
    return robotCopy

def sumOfQuadrant(q: list[list[tuple[int, int]]]):
    return sum(sum(len(j) for j in i) for i in q)
    
                

for line in lines:
    px, py, vx, vy = map(int, re.fullmatch(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line).groups())
    robots[py][px].append((vx, vy))
for i in range(100):
    robots = moveRobots(robots)
    
q1 = sumOfQuadrant([r[n//2+1:] for r in robots[:m//2]])
q2 = sumOfQuadrant([r[:n//2] for r in robots[:m//2]])
q3 = sumOfQuadrant([r[:n//2] for r in robots[m//2+1:]])
q4 = sumOfQuadrant([r[n//2+1:] for r in robots[m//2+1:]])
ans = q1 * q2 * q3 * q4
print(ans)