with open("input.txt") as f:
    lines = f.read().split("\n") 

l1 = []
l2 = []
for line in lines:
    l1Loc, l2Loc = map(int, line.split())
    l1.append(l1Loc)
    l2.append(l2Loc)
summ = sum(abs(i-j) for i,j in zip(sorted(l1), sorted(l2)))
print(summ)