with open("input.txt") as f:
    lines = f.read().splitlines()
    
safe = 0
for line in lines:
    intLine = list(map(int, line.split()))
    lenn = len(intLine)
    for k in range(lenn):
        currLine = intLine[:k] + intLine[k+1:]
        l1, l2 = currLine, currLine[1:]
        isIncreasing = l1[1] - l1[0] > 0
        for i, j in zip(l1, l2):
            if not 1<=abs(i-j)<=3 or isIncreasing and (j - i)<0 or not isIncreasing and (j - i)>0:
                break
        else:
            safe+=1
            break
        
print(safe)