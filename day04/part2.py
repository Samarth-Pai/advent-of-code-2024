with open("input.txt") as f:
    lines = f.read().splitlines()
    
nRows, nCols = len(lines), len(lines[0])

totalCombs = 0
for i in range(1, nRows-1):
    for j in range(1, nCols-1):
        if lines[i][j] == "A":
            totalCombs += (lines[i-1][j-1] + lines[i+1][j+1] in ["MS", "SM"]
                           and lines[i+1][j-1] + lines[i-1][j+1] in ["MS", "SM"])
print(totalCombs)