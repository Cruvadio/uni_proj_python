class Dungeon (dict):
    def __missing__(self, key):
        return 0



def find_tunnel(d, k, f):
    watched = set()
    queue = [k]
    while queue:
        k =  queue.pop(0)
        if d[k].intersection(d[f]):
            return True
        for c in d[k]:
            if c in watched:
                continue
            watched.add(c)
            queue.append(c)
    return False

dungeons = Dungeon()
while True:
    string = input()
    if " " not in string:
        dungeon2 = input()
        if not dungeons[string] or not dungeons[dungeon2]:
            print("NO")
        elif find_tunnel(dungeons, string, dungeon2):
            print("YES")
        else:
            print("NO")
        break
    dungeon1, dungeon2 = string.split(" ")
    if not dungeons[dungeon1]:
        dungeons[dungeon1] = set((dungeon2,))
    else:
        dungeons[dungeon1].add(dungeon2)

    if not dungeons[dungeon2]:
        dungeons[dungeon2] = set((dungeon1,))
    else:
        dungeons[dungeon2].add(dungeon1)