first_line = input()
field = []
rect_cords = []
while True:
    line = input()
    if line == first_line:
        break
    field.append(line)

num_rec = 0
f = k = 0
for i in range(len(field)):
    for j in range(len(line)):
        if field[i][j] == '#':
            f = 1
            k = i
            while field[k][j] == '#':
                field[k] = field[k][:j] + '.' + field[k][j + 1:]
                k += 1
                if k >= len(field):
                    break
        elif f == 1:
            num_rec += 1
            f = 0

print(num_rec)
