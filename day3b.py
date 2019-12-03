day3 = [
    ["R8", "U5", "L5", "D3"],
    ["U7", "R6", "D4", "L4"]
]

loc = [0, 0]

for day in day3:
    for d in day:
        move = d[0]
        step = int(d[1:])

        if move == "U":


