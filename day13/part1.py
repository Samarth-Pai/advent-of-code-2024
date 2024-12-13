import re
with open("input.txt") as f:
    lines = f.read().splitlines()
    
def calculateTokens(machine: dict) -> int:
    px, py = machine["p"]
    ax, ay = machine["A"]
    bx, by = machine["B"]
    possiblex, possibley = 0, 0
    for i in range(1, 101):
        jx = (px - i*ax)/bx
        jy = (py - i*ay)/by
        if jx%1==0 and jy%1 == 0 and jx == jy:
            possiblex, possibley = i, int(jx)
            break
        
    if possiblex:
        return possiblex*3 + possibley
    return 0
            
machine = {}
totalTokens = 0
for line in lines:
    if r:=re.fullmatch(r"Button A: X\+(\d+), Y\+(\d+)", line):
        x, y = map(int, r.groups())
        machine["A"] = (x, y)
    elif r:=re.fullmatch(r"Button B: X\+(\d+), Y\+(\d+)", line):
        x, y = map(int, r.groups())
        machine["B"] = (x, y)
    elif r:=re.fullmatch(r"Prize: X=(\d+), Y=(\d+)", line):
        x, y = map(int, r.groups())
        machine["p"] = (x, y)
        tokens = calculateTokens(machine)
        totalTokens+=tokens
        machine = {}
        
print(totalTokens)