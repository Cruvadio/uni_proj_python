k = int(input())
if k == 0:
    print("0")
elif k == 1:
    print("1")
else:
    p = 10
    while (k * p - k**2 ) % (k * 10 - 1) != 0:
        p *= 10

    n = (k * p - k**2 ) // (k * 10 - 1)
    print(n*10 + k)




