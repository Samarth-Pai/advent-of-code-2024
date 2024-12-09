with open("input.txt") as f:
    line = f.read()
    
disk = []
for en, d in enumerate(line):
    if en%2:
        disk.extend(["."]*int(d))
    else:
        enBy2 = str(en//2)
        disk.append((enBy2, )*int(d))
        # disk.extend([enBy2 for _ in range(int(d))])
        
j = len(disk) - 1
while not isinstance(disk[j], tuple):
    j-=1
    
# print(disk)
while j>=0:
    i1 = 0
    lenn = 0
    tLen = len(disk[j])
    for i in range(j):
        if disk[i] == ".":
            if lenn == 0:
                i1 = i
                lenn = 1
            else:
                lenn+=1
            if lenn>=tLen:
                tup = disk[j]
                disk.pop(j)
                for _ in range(lenn):
                    disk.insert(j, ".")
                for _ in range(lenn):
                    disk.pop(i1)
                disk.insert(i1, tup)
                lenn = 0
                break
        else:
            lenn = 0
    j-=1
    while j>=0 and not isinstance(disk[j], tuple):
        j-=1
    
finalDisk = []
for ele in disk:
    if isinstance(ele, tuple):
        finalDisk.extend(ele)
    else:
        finalDisk.append(ele)
      
summ = 0
for en, num in enumerate(finalDisk):
    if num.isdigit(): summ+=int(num)*en
    
print(summ)