from math import *
def distance (a, b):
    return (b[0] - a[0])**2 + (b[1] - a[1])**2 + (b[2] - a[2])**2


galaxies = dict()
while True:
    string = input()
    if string == ".":
        break
    first, second, third, name = string.split()
    galaxies[(float(first), float(second), float(third))] = name

max_d = 0
max_names = ""
watched = set()

for key, value in galaxies.items():
    watched.add(key)
    for k, v in galaxies.items():
        if k in watched:
            continue
        dist = distance(k, key)
        if dist >= max_d:
            max_d = dist
            max_names = min(v, value) + " " + max(v, value)

print(max_names)