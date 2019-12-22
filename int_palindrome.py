a = n = int(input())
b, ten = 0, 1
while True:
    n = n // 10
    if n == 0:
        break
    ten *= 10
n = a
while n != 0:
    last = n % 10
    b += ten * last
    n = n // 10
    ten //= 10
if b == a:
    print("YES")
else:
    print("NO")

