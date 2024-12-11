from functools import cache
with open("input.txt") as f:
    line = f.read()
    
nums = [int(s) for s in line.split()]
def blink(stones: list[int]) -> list[int]:
    newStone = []
    for stone in stones:
        newStone.extend(action(stone))
    return newStone
            
@cache
def action(stone: int) -> list[int]:
    if stone==0:
        return [1]
    elif (l:=len(s:=str(stone)))%2 == 0:
        leftHalf = s[:l//2]
        rightHalf = s[l//2:]
        return [int(leftHalf), int(rightHalf)]
        
    else:
        return[stone*2024]
    
for _ in range(25):
    nums = blink(nums)
    
ans = len(nums)
print(ans)