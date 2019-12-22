a = eval(input())
x = []
for i in a:
    x.append((i[0], False))
    x.append((i[1], True))

x.sort(key= lambda k: k[0])
c = 0
result = 0
for i in range(len(x)):
    if c and i:
        result += abs(x[i][0] - x[i - 1][0])
    if x[i][1]:
        c += 1
    else:
        c -= 1
print(result)