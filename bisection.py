from math import *

expr = input()
a, b = eval(input())
c = (a + b) / 2
eps = 0.000001
while abs(a - b) > eps:
    x = a
    left = eval(expr)
    if left == 0:
        print(a)
        break
    x = b
    right = eval(expr)
    if right == 0:
        print(b)
        break
    x = c
    right = eval(expr)
    if right == 0:
        print(c)
        break
    if right * left < 0:
        b = c
    else:
        a = c
    c = (a + b) / 2
else:
    print(c)

