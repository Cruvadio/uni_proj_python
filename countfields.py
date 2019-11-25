def fcounter(c, *args):
    obj = c(*args)
    cm = [x for x in dir(c) if callable(getattr(c, x)) and "__" not in x and x[0] != "_"]
    cf = [x for x in dir(c) if not callable(getattr(c, x)) and "__" not in x and x[0] != "_"]
    om = [x for x in dir(obj) if callable(getattr(obj, x)) and "__" not in x and x[0] != "_" and (x not in dir(c) or not callable(getattr(c, x)))]
    of = [x for x in dir(obj) if not callable(getattr(obj, x)) and "__" not in x and x[0] != "_" and (x not in dir(c) or callable(getattr(c, x)))]
    return cm, cf, om, of