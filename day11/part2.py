from functools import cache
with open("input.txt") as f:
    line = f.read()

@cache
def nSplits(stone: int, loopNo = 75):
    if loopNo==0:
        return 1
    if stone==0:
        return nSplits(1, loopNo-1)
    elif (l:=len(s:=str(stone)))%2 == 0:
        leftHalf = int(s[:l//2])
        rightHalf = int(s[l//2:])
        return nSplits(leftHalf, loopNo - 1) + nSplits(rightHalf, loopNo - 1)
    else:
        return nSplits(stone*2024, loopNo - 1)
        

nums = [int(stone) for stone in line.split()]
    
ans = sum(map(nSplits, nums))
print(ans)