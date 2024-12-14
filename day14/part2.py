import re
from copy import deepcopy
with open("input.txt") as f:
    lines = f.read().splitlines()
    
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

def isEasterEgg(robots):
    for i in robots:
        for j in i:
            if len(j)>=2:
                return False
    return True

for line in lines:
    px, py, vx, vy = map(int, re.fullmatch(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line).groups())
    robots[py][px].append((vx, vy))
    
i = 0
while not isEasterEgg(robots):
    robots = moveRobots(robots)
    i+=1
print(i)