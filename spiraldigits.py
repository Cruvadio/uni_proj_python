M, N = eval(input())

a, k, count, arr, r = 0, 0, 0, [[0 for j in range(M)]for i in range(N)], range(10)
min = 0
if N > M:
    if M % 2 == 0 :
        min = M // 2 - 1
    else:
        min = M // 2
else:
    if N % 2 == 0:
        min = N // 2 - 1
    else:
        min = N // 2
i = j = 0
while count < N*M:
    while k <= min:
        while j < M - k:
            arr[i][j] = a
            a += 1
            if a >= len(r):
                a = 0
            j += 1
            count += 1
        if N != M:
            if count >= N * M:
                break
        j -= 1
        i += 1
        while i < N - k:
            arr[i][j] = a
            a += 1
            if a >= len(r):
                a = 0
            i += 1
            count += 1
        if N != M:
            if count >= N*M:
                break
        i -= 1
        j -= 1
        while j >= k:
            arr[i][j] = a
            a += 1
            if a >= len(r):
                a = 0
            count += 1
            j -= 1
        if N != M:
            if count >= N * M:
                break
        k += 1
        j += 1
        i -= 1
        while i >= k:
            arr[i][j] = a
            a += 1
            if a >= len(r):
                a = 0
            count += 1
            i -= 1
        if N != M:
            if count >= N * M:
                break
        j += 1
        i += 1

for row in arr:
    for col in row:
        print(col, end=" ")
    print()
