def nonify (f):
    def newfun(*args, **kwargs):
        res = f(*args, **kwargs)
        if not res:
            res = None
        return res
    return newfun
