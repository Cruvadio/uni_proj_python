tup = eval(input())
conveyor = []
i = 0
for item in tup:
    if type(item) is tuple:
        conveyor.extend(item)
    elif type(item) is int:
        if i + item > len(conveyor):
            break
        print(tuple(conveyor[i:i + item]))
        i += item
    else:
        print("Unknown type.")