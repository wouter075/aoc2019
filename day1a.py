import math

lines = [int(line.rstrip('\n')) for line in open("day1a.txt")]

t1 = 0
t2 = 0

for l in lines:
    t1 = t1 + math.floor(l / 3) - 2
    t3 = l

    while t3 > 5:
        t3 = math.floor(t3 / 3) - 2
        t2 = t2 + t3

print("- part 1 ----")
print(t1)
print("- part 2 ----")
print(t2)