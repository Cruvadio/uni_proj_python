a = int(input())
for i in range(2, a):
    n = a
    while n != 1:
        if n % i != 0:
            break
        n //= i
    else:
        print("YES")
        break;
else:
    print("NO")
