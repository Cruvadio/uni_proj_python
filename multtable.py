N, M = eval(input())

splitter = "".ljust(M, "=")
equation = "{{:{}s}}"
temp = "{{:<{}s}}"
multi = "{0} * {1}"
max_str = equation.format(len(multi.format(N, N)) + 1).format(multi.format(N, N)) + "= {}".format(N * N)
len_max_str = len(max_str) + 1
num_cols = (M - 2) // (len_max_str + 1)
#while True:
#    if M % len_max_str <= 2:
#        num_cols = M // len_max_str
#        if M % len_max_str >= 1:
#            multi = " " + multi
#        break
#    len_max_str += 1
temp = temp.format(len_max_str)
lenN = len(str(N))
k = 1
flag = False
strings = []
count = 0
while True:
    for j in range(k, N + 1, num_cols):
        len_max_num = len(multi.format(j, N))
        tabs = "".ljust(lenN - len(str(j)), " ")
        tmp = equation.format(len_max_num)
        for i in range(1, N + 1):
            end = ''
            sent = tabs + tmp.format(multi.format(j, i)) + " = {}".format(j * i)
            final = temp.format(sent) if j % num_cols == 0 or j == N else temp.format(sent) + "| "
            if k == 1:
                strings.append(final)
            else:
                strings[count] += final
                count += 1
    k += 1
    count = 0
    if k > num_cols:
        break
count = 0
for string in strings:
    if count % N == 0:
        print(splitter)
    print(string)
    count += 1
print(splitter)

# while True:
#     for i in range(1, N + 1):
#         for j in range(1, num_cols + 1):
#             num = k + j
#             len_max_num = len(multi.format(num, N))
#             end = ''
#             if num > N:
#                 flag = True
#                 break
#             if j != num_cols and num != N:
#                 end = '| '
#             sent = "".ljust(lenN - len(str(num)), " ") + equation.format(len_max_num).format(multi.format(num, i)) + " = {}".format(num * i)
#             print(temp.format(sent), end=end)
#         print()

    # k += num_cols
    # print(splitter)
    # if flag or k >= N:
    #     break
