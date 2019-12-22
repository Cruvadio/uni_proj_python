flag = True
first = set()
second = set()
while True:
    string = input()
    if not string:
        break
    if flag:
        first = set.union(set([x for x in string]), first)
    else:
        second = set.union(set([x for x in string]), second)
    flag = not flag

if len(first) > len(second):
    print("Mumbo")
else:
    print("Jumbo")