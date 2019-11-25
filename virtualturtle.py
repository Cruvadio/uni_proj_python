def turtle (coord, direction):
    new_coord = list(coord)
    c = yield coord
    while True:
        if c == 'f':
            if not direction:
                new_coord[0] += 1
            elif direction == 1:
                new_coord[1] += 1
            elif direction == 2:
                new_coord[0] -= 1
            elif direction == 3:
                new_coord[1] -= 1
        elif c == 'l':
            direction = (direction + 1) % 4
        elif c == 'r':
            direction = (direction - 1) if direction else 3
        c = yield new_coord