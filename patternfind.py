string = input()
pattern = input()


index = 0
flag = True
while flag:
    first_a = pattern.find("@")
    if first_a == -1:
        print(string.find(pattern))
        break
    index = string.find(pattern[:first_a], index)
    if index == -1:
        print(-1)
        break
    i = index + len(pattern[:first_a]) + 1
    for c in pattern[first_a + 1:]:
        if c == "@":
            i += 1
            continue
        if len(string) <= i:
            print(-1)
            flag = False
            break
        if string[i] != c:
            index += 1
            break
        i += 1
    else:
        print(index)
        break



