def pigen():
    n = 0
    s = 0
    while True:
        s +=((-1)**n)/(2 * n + 1)
        yield s * 4
        n += 1