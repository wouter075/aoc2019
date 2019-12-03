# day3 = [
#     ["R8", "U5", "L5", "D3"],
#     ["U7", "R6", "D4", "L4"]
# ]

day3 = [
    ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
    ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]
]


def printgrid(g):
    grid = len(g)
    for x in range(0, grid):
        line = ""
        for y in range(0, grid):
            line = line + g[x][y]
        print(str(grid - (x + 1)).ljust(5) + "| " + line)


def creategrid(g):
    wires = {}
    for x in range(0, g):
        wires[x] = {}
        for y in range(0, g + 1):
            wires[x][y] = " . "
    return wires


# setup
grid = 500

# create grid
wires = creategrid(grid)

# magic
cross = False
crossings = []

for day in day3:
    x = grid - 2
    y = 1

    wires[x][y] = " O "

    for d in day:
        move = d[0]
        lenght = int(d[1:])

        # place on grid
        if move == "U":
            for xm in range(1, lenght + 1):
                x = x - 1

                if cross:
                    if wires[x][y] == " . ":
                        pass
                    else:
                        crossings.append([x, y])

                if xm == lenght:
                    wires[x][y] = " + "
                else:
                    wires[x][y] = " | "

        if move == "D":
            for xm in range(1, lenght + 1):
                x = x + 1

                if cross:
                    if wires[x][y] == " . ":
                        pass
                    else:
                        crossings.append([x, y])

                if xm == lenght:
                    wires[x][y] = " + "
                else:
                    wires[x][y] = " | "

        if move == "R":
            for ym in range(1, lenght + 1):
                y = y + 1

                if cross:
                    if wires[x][y] == " . ":
                        pass
                    else:
                        crossings.append([x, y])

                if ym == lenght:
                    wires[x][y] = " + "
                else:
                    wires[x][y] = " - "

        if move == "L":
            for ym in range(1, lenght + 1):
                y = y - 1

                if cross:
                    if wires[x][y] == " . ":
                        pass
                    else:
                        crossings.append([x, y])

                if ym == lenght:
                    wires[x][y] = " + "
                else:
                    wires[x][y] = " - "

    cross = True

# printgrid(wires)

for c in crossings:
    x, y = c
    tot = 0
    for s in range(2, grid - x - 1):
        tot = tot + 1
    for s in range(1, y + 1):
        tot = tot + 1

    print("--")
    print(tot)
    print("--")
