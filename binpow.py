def BinPow (a, N, fun):
    if N == 1:
        return a
    if N % 2 == 0:
        return fun(BinPow(a, N//2, fun), BinPow(a, N//2, fun))
    return fun(a, BinPow(a, N - 1, fun))