with open("input.txt") as f:
    line = f.read()
    
disk = []
for en, d in enumerate(line):
    if en%2:
        disk.extend(["."]*int(d))
    else:
        enBy2 = str(en//2)
        disk.extend([enBy2 for _ in range(int(d))])
        
i = disk.index(".")
j = len(disk)-1

while not disk[j].isdigit():
    j-=1
    
while i<j:
    disk[i], disk[j] = disk[j], disk[i]
    i+=1
    j-=1
    while disk[i]!=".":
        i+=1
    while not disk[j].isdigit():
        j-=1
        
summ = 0
for en, num in enumerate(disk):
    if num==".":
        break
    summ+=int(num)*en
    
print(summ)