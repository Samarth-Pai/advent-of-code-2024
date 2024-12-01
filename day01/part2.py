from collections import Counter
with open("input.txt") as f:
    lines = f.read().split("\n") 

l1 = []
l2 = []
for line in lines:
    l1Loc, l2Loc = map(int, line.split())
    l1.append(l1Loc)
    l2.append(l2Loc)

freq = Counter(l2)
summ = sum(i*freq.get(i, 0) for i in l1)
print(summ)