from operator import mul
from bisect import bisect_left
import re
with open("input.txt") as f:
    line = f.read()
    
dos = re.finditer(r"do\(\)", line)
donts = re.finditer(r"don't\(\)", line)

doIndices = [0] + [m.start() for m in dos]
dontIndices = [m.start() for m in donts]
safeRanges = []
for do in doIndices:
    try:
        safeRanges.append((do, dontIndices[bisect_left(dontIndices, do)]))
    except IndexError:
        safeRanges.append((do, len(line)-1))
        break

matches = re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", line)
summ = 0
for match in matches:
    for sr, er in safeRanges:
        if sr<=match.start()<=er:
            summ+=mul(*map(int, match.groups()))
            break
print(summ)
