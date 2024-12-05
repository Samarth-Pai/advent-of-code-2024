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
    
invalidSections = []
sectionList = [sec.split(",") for sec in secondSection]
for section in sectionList:
    for i, j in zip(section, section[1:]):
        if j not in pageDict[i]:
            invalidSections.append(section)
            break
        
midSum = 0
for sec in invalidSections:
    linkDict = defaultdict(int)
    for n in sec:
        for p in pageDict[n]:
            linkDict[n]+=p in sec
    sortedSec = sorted(sec, key = lambda x:-linkDict[x])
    midSum+=int(sortedSec[len(sortedSec)//2])

print(midSum)