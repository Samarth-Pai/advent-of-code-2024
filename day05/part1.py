from collections import defaultdict
with open("input.txt") as f:
    lines = f.read().splitlines()
    
firstDone = False
firstSection, secondSection = [], []
for line in lines:
    if line == "":
        firstDone = True
        continue
    if not firstDone:
        firstSection.append(line)
    else:
        secondSection.append(line)
        
pageDict = defaultdict(list)
for page in firstSection:
    x, y = page.split("|")
    pageDict[x].append(y)
    
validSections = []
sectionList = [sec.split(",") for sec in secondSection]
for section in sectionList:
    for i, j in zip(section, section[1:]):
        if j not in pageDict[i]:
            break
    else:
        validSections.append(section)

middles = [sec[len(sec)//2] for sec in validSections]
ans = sum(map(int, middles))
print(ans)