def fix(n):
    def decorator_maker(f):
        def decorator_wrapper(*args, **kwargs):
            new_args = []
            for arg in args:
                if type(arg) == float:
                    new_args.append(round(arg, n))
                else:
                    new_args.append(arg)
            for k, v in kwargs.items():
                if type(v) == float:
                    kwargs[k] = round(v, n)
                else:
                    kwargs[k] = v
            return round(f(*new_args, **kwargs), n)
        return decorator_wrapper
    return decorator_maker
