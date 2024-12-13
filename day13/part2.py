import re
with open("input.txt") as f:
    lines = f.read().splitlines()
    
def calculateTokens(machine: dict) -> int:
    px, py = machine["p"]
    px, py = px+10000000000000, py+10000000000000
    ax, ay = machine["A"]
    bx, by = machine["B"]
    low , high = 1, min(px, py)
    j1 = ((px + py) - (ax + ay))/(bx + by)
    j2 = ((px + py) - 2*(ax + ay))/(bx + by)
    isInreasing = 1*ax + j1*bx < 2*ax + j2*bx
    if isInreasing:
        while low<=high:
            i = (low + high)//2
            j = ((px + py) - i*(ax + ay))/(bx + by)
            rpx = i*ax + j*bx
            if  rpx < px:
                low = i + 1
            elif rpx > px:  
                high = i - 1
            else:
                return i*3 +  int(j)
    else:
        while low<=high:
            i = (low + high)//2
            j = ((px + py) - i*(ax + ay))/(bx + by)
            rpx = i*ax + j*bx
            if  rpx > px:
                low = i + 1
            elif rpx < px:
                high = i - 1
            else:
                return i*3 +  int(j)
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