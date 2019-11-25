def return_cords(x, y, negY, MinX, MinY, cols):
    x0 = abs(x - MinX) if abs(x - MinX) != cols else abs(x - MinX) - 1
    y0 = abs(y - MinY) * cols
    cell = x0 + y0
    return cell // cols, cell % cols if abs(x - MinX) != cols else cell % cols + 1


coords = []
while True:
    string = input()
    if "0 0 0 0" in string:
        break
    x, y, lenX, lenY, symb = string.split(" ")
    if int(lenY) and int(lenX):
        coords.append((int(x) - 1, int(y) - 1, int(lenX), int(lenY), symb))

MaxlenX = max(coords, key=lambda x: x[0] + x[2])
MaxlenY = max(coords, key=lambda x: x[1] + x[3])
MinlenX = min(coords, key=lambda x: x[0] + x[2])
MinlenY = min(coords, key=lambda x: x[1] + x[3])

MaxX = max(max(coords, key=lambda x: x[0])[0], MaxlenX[0] + MaxlenX[2])
MaxY = max(max(coords, key=lambda x: x[1])[1], MaxlenY[1] + MaxlenY[3])
MinX = min(min(coords, key=lambda x: x[0])[0], MinlenX[0] + MinlenX[2])
MinY = min(min(coords, key=lambda x: x[1])[1], MinlenY[1] + MinlenY[3])

cols = MaxX - MinX
rows = MaxY - MinY

field = ["".ljust(cols, ".") for _ in range(rows)]

for cord in coords:
    x, y, lenX, lenY, symb = cord
    startX, startY = return_cords(x, y, True if lenY < 0 else False, MinX, MinY, cols)
    endX, endY = return_cords(x + lenX, y + lenY, True if lenY < 0 else False, MinX, MinY, cols)
    i, i1 = min(startX, endX), max(startX, endX)
    j, j1 = min(startY, endY), max(startY, endY)

    while i < i1 and i < len(field):
        field[i] = field[i][:j] + "".ljust(j1-j, symb) + field[i][j1:]
        i += 1

for f in field:
    print(f)
