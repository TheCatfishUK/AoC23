data = 0

if data == 0:
    f = open("test.py")
else:
    f = open("input.py")

grid = []

for line in f:
    line = line.strip()
    gridline = []
    for a in range(len(line)):
        gridline.append({"id":line[a], "c":0, "s":0})
    grid.append(gridline)

# Who knows what I'm actually doing here

for a in range(len(grid)):
    for b in range(len(grid[a])):
        if grid[a][b]['c'] == 0:
            # print(grid[a][b]['c'])
            for i in range(-1,2):
                for j in range(-1,2):
                    try:
                        grid[a+i][b+j]['c']
                    except:
                        pass
                    else:
                        try:
                            int(grid[a+i][b+j]['id'])
                        except:
                            if grid[a+i][b+j]['id'] != '.':
                                grid[a][b]['s'] = 1

for a in grid:
    print(a)
