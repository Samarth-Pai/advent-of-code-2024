from itertools import product
with open("input.txt") as f:
    lines = f.read().splitlines()
    
def isPossible(target: int, nums: list[int]):
    if sum(nums) == target:
        return True
    n = len(nums)
    for opers in product(("*", "+", "||"), repeat=n-1):
        total = nums[0]
        for k, op in zip(nums[1:], opers):
            if op=="*":
                total*=k
            elif op=="||":
                total = int(str(total)+str(k))
            else:
                total+=k
        if total==target:
            return True
    return False

summ = 0
for line in lines:
    target, nums = line.split(":")
    target = int(target)
    nums = list(map(int, nums.split()))
    summ+=isPossible(target, nums)*target

print(summ)