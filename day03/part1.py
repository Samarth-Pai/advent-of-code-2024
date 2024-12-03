from operator import mul
import re
with open("input.txt") as f:
    line = f.read()
    
matches = re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", line)
summ = sum(mul(*map(int, m.groups())) for m in matches)
print(summ)