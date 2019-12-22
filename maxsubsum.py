num = int(input())
p_flag = False
sum = max_sum = max_neg = 0
if num < 0:
    max_neg = num
else:
    p_flag = True
while num != 0:
    if num < 0:
        if max_neg < num:
            max_neg = num
    else:
        p_flag = True
    sum += num
    if sum < 0:
        sum = 0
        max_sum = 0
    else:
        if max_sum < sum:
            max_sum = sum
    num = int(input())
if not p_flag:
    print(max_neg)
else:
    print(max_sum)