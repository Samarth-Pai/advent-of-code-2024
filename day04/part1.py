with open("input.txt") as f:
    lines = f.read().splitlines()
    
nRows, nCols = len(lines), len(lines[0])

def matches(x, y):
    combs = 0

    # check north
    if x>2 and  "".join(lines[x-i][y] for i in range(4)) == "XMAS":
        combs+=1 
    # Check north east
    if x>2 and y<nCols-3 and "".join(lines[x-i][y+i] for i in range(4)) == "XMAS":
        combs+=1
    # Check east
    if y<nCols-3 and lines[x][y:y+4] == "XMAS":
        combs+=1
    # Check south east
    if x<nRows-3 and y<nCols-3 and "".join(lines[x+i][y+i] for i in range(4)) == "XMAS":
        combs+=1
    # Check south
    if x<nRows-3 and "".join(lines[x+i][y] for i in range(4)) == "XMAS":
        combs+=1
    # Check south west
    if y>2 and x<nRows-3 and "".join(lines[x+i][y-i] for i in range(4)) == "XMAS":
        combs+=1
    # Check west
    if y>2 and "".join(lines[x][y-i] for i in range(4)) == "XMAS":
        combs+=1
    # Check north west
    if x>2 and y>2 and "".join(lines[x-i][y-i] for i in range(4)) == "XMAS":
        combs+=1
    return combs
    
totalCombs = 0
for i in range(nRows):
    for j in range(nCols):
        if lines[i][j] == "X":
            totalCombs+=matches(i ,j)
            
print(totalCombs)