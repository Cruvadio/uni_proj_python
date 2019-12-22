def maxfun(arr, *args):
    return args[len(args) - max(enumerate([sum(arg(x) for x in arr) for arg in reversed(args)]), key=lambda key: key[1])[0] - 1]