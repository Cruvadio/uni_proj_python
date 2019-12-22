class DivStr ():
    def __init__(self, string):
        self._string = str(string)
    def capitalize(self):
        return DivStr(self._string.capitalize())
    def casefold(self):
        return DivStr(self._string.casefold())
    def center(self,*args):
        args = [str(a) if type(a) == DivStr else a for a in args]
        return DivStr(self._string.center( *args))
    def count(self, *args):
        args = [str(a) if type(a) == DivStr else a for a in args]
        return self._string(*args)
    def join(self,*args):
        args = [str(a) if type(a) == DivStr else a for a in args]
        return DivStr(self._string.join(*args))
    def encode(self,*args):
        args = [str(a) if type(a) == DivStr else a for a in args]
        return self._string.encode(*args)
    def endswith(self, *args):
        args = [str(a) if type(a) == DivStr else a for a in args]
        return  DivStr(self._string.endswith(*args))
    def expandtabs(self,*args):
        args = [str(a) if type(a) == DivStr else a for a in args]
        return DivStr(self._string.expandtabs(*args))
    def find(self, *args):
        args = [str(a) if type(a) == DivStr else a for a in args]
        return self._string.find(*args)
    def format(self, *args: object, **kwargs: object):
        args = [str(a) if type(a) == DivStr else a for a in args]
        return  DivStr(self._string.format(*args, **kwargs))
    def format_map(self, map):
        return DivStr(self._string.format_map(map))
    def index(self, *args):
        return self._string.index(*args)
    def isalnum(self):
        return self._string.isalnum()
    def isascii(self):
        return self._string.isascii()
    def isalpha(self):
        return self._string.isalpha()
    def isdecimal(self):
        return self._string.isdecimal()
    def isdigit(self):
        return self._string.isdigit()
    def isidentifier(self):
        return self._string.isidentifier()
    def islower(self):
        return self._string.islower()
    def isnumeric(self):
        return self._string.isnumeric()
    def isprintable(self):
        return self._string.isprintable()
    def isspace(self):
        return self._string.isspace()
    def istitle(self):
        return self._string.isspace()
    def isupper(self):
        return self._string.isupper()
    def ljust(self, *args):
        args = [str(a) if type(a) == DivStr else a for a in args]
        return DivStr(self._string.ljust(*args))
    def lower(self):
        return DivStr(self._string.lower())
    @staticmethod
    def maketrans(x):
        return str.maketrans(x)
    def partition(self, sep):
        return self._string.partition(self, str(sep))
    def replace(self, *args):
        args = [str(a) if type(a) == DivStr else a for a in args]
        return DivStr(self._string.replace(*args))
    def startswith(self,*args):
        args = [str(a) if type(a) == DivStr else a for a in args]
        return self._string.startswith(*args)
    def strip(self, *args):
        args = [str(a) if type(a) == DivStr else a for a in args]
        return DivStr(self._string.strip(*args))
    def swapcase(self):
        return DivStr(self._string.swapcase())
    def title(self):
        return DivStr(self._string.title())
    def translate(self, *args):
        args = [str(a) if type(a) == DivStr else a for a in args]
        return DivStr(self._string.translate(*args))
    def upper(self):
        return DivStr(self._string.upper())
    def zfill(self, width):
        return DivStr(self._string.zfill(width))
    def __add__(self, other):
        return DivStr(self._string + other)
    def __mul__(self, other):
        return DivStr(self._string * other)
    def __getitem__(self, item):
        return DivStr(self._string.__getitem__(item))
    def __truediv__(self, other):
        return DivStr(self._string[:len(self._string)//other])
    def __len__(self):
        return self._string.__len__()
    def __str__(self):
        return self._string
    def __pow__(self, power, modulo=None):
        return self._string.__pow__(power, modulo)
