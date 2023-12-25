def findNext(cur, x, y):
    if cur == "7":
        return [[x-1, y], [x, y+1]]
    elif cur == "J":
        return [[x-1, y], [x, y-1]]
    elif cur == "F":
        return [[x+1, y], [x, y+1]]
    elif cur == "L":
        return [[x+1, y], [x, y-1]]
    elif cur == "-":
        return [[x-1, y], [x+1, y]]
    elif cur == "|":
        return [[x, y+1],[x, y-1]]

with open("maze.txt") as f:
    pipes = f.read().splitlines()

for i in range(len(pipes)):
    if "S" in pipes[i]:
        start = [pipes[i].index('S'), i]

stepmap = [['.'] * len(pipe) for pipe in pipes]
steps, curQueue, nextQueue = 1, [], []

#Part 2 to get the S into its proper shape
shapeFlag = 0
shapeMap = {11: "-", 101: "J", 1001: "7", 110: "L", 1010: "F", 1100: "|"}

if pipes[start[1]][start[0] - 1] in ["F", "L", "-"]:
    shapeFlag += 1
    curQueue.append((start[0]-1, start[1]))
if pipes[start[1]][start[0] + 1] in ["J", "7", "-"]:
    shapeFlag += 10
    curQueue.append((start[0]+1, start[1]))
if pipes[start[1] - 1][start[0]] in ["F", "7", "|"]:
    shapeFlag += 100
    curQueue.append((start[0], start[1]-1))
if pipes[start[1]+1][start[0]] in ["J", "L", "|"]:
    shapeFlag += 1000
    curQueue.append((start[0], start[1]+1))

stepmap[start[1]][start[0]] = shapeMap[shapeFlag]

while curQueue:
    x, y = curQueue.pop()
    stepmap[y][x] = pipes[y][x]
    nextSteps = findNext(pipes[y][x], x, y)
    for step in nextSteps:
        if stepmap[step[1]][step[0]] == ".":
            nextQueue.append(step)

    if not curQueue:
        curQueue = nextQueue
        nextQueue = []
        steps += 1

newMap, newlines = [], []
for j, line in enumerate(stepmap):
    i = 0

    newline = []
    while i < len(line):
        if line[i] in ["L", "F", "-"]: line.insert(i+1, "-")
        else: line.insert(i+1, ".")
        if line[i] in ["F", "|", "7"]: newline += ["|", "."]
        else: newline += [".", "."]
        i += 2
    newlines.append(newline)

bigmap = [None] * (len(stepmap)*2)
bigmap[::2] = stepmap #I accidentally stumbled into this lol
bigmap[1::2] = newlines
bigmap.insert(0, ["."] * len(bigmap[0]))

curQueue = [[0,0]]
while curQueue:
    x, y = curQueue.pop()
    bigmap[y][x] = "O"
    try:
        if bigmap[y][x-1] == ".":
            curQueue.append([x-1, y])
    except: pass
    try:
        if bigmap[y][x+1] == ".":
            curQueue.append([x+1, y])
    except:pass
    try:
        if bigmap[y+1][x] == ".":
            curQueue.append([x, y+1])
    except:pass
    try:
        if bigmap[y-1][x] == ".":
            curQueue.append([x, y-1])
    except:pass

#for line in stepmap:
#    print(" ".join([str(x) for x in line[::2]]))

# print(steps-1)
print(sum(line[::2].count(".") for line in stepmap))