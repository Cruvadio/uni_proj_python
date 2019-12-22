def sizer (cl):
    class Descriptor:
        value = 0
        def __get__(self, instance, owner):
            if hasattr(owner, "__len__"):
                return len(instance)
            else:
                return abs(int(instance))
    class New(cl):
        size = Descriptor()
    return New
