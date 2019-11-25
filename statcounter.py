class Counter(dict):
    def __missing__(self, key):
        return 0


def statcounter ():
    funcs = Counter()
    f = yield funcs
    while True:

        def wrapper(*args, i=f, **kwargs):
            funcs[i] += 1
            return i(*args, **kwargs)

        f = yield wrapper
