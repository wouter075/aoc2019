with open('day8.txt', 'r') as file:
    data = file.read().replace('\n', '')


def wrap(s, w):
    return [s[i:i + w] for i in range(0, len(s), w)]


width = 25
tall = 6
pixels = width * tall
start = 0
zeros = {}
ones = {}
twos = {}
maxed = 100
lm = 0

layers = wrap(data, pixels)

for l in layers:
    zeros[start] = l.count("0")
    ones[start] = l.count("1")
    twos[start] = l.count("2")

    if l.count("0") < maxed:
        maxed = l.count("0")
        lm = start

    start += 1

print(zeros)
print(maxed)
print(lm)
print(ones[lm] * twos[lm])