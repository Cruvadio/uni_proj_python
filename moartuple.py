def moar (a, b, n):
    count_a = count_b = 0
    for x in a:
        if x % n == 0:
            count_a += 1
    for x in b:
        if x % n == 0:
            count_b += 1

    return count_a > count_b