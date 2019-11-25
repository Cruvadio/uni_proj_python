import fractions
import itertools
import math
class sausage:
    def __init__(self, *args):
        self.mince = "pork!"
        self.size = fractions.Fraction(1)
        if len(args) > 0:
            self.mince = args[0]
        if len(args) > 1:
            self.size = fractions.Fraction(args[1])

    def __str__(self):
        n = self.size.__floor__()
        num_chars = math.ceil(12 * (self.size - n))
        top = nachinka = bottom = ''
        if not self.size or self.size < 0 or self.size.__round__() < 1:
            return "/|\n||\n||\n||\n\\|"
        for i in range(n + 1 if self.size.denominator != 1 else n):
            top += '/{}\\'.format("".join(itertools.repeat('-', 12))) if i < n or num_chars == 12 else '/{}|'.format(
            "".join(itertools.repeat('-', math.ceil(num_chars))))
        for _ in range(3):
            for i in range(n + 1 if self.size.denominator != 1 else n):
                nachinka += '|{}|'.format(("".join(itertools.repeat(self.mince, math.ceil(
                    12/len(self.mince) if i < n or num_chars == 12 else num_chars/len(self.mince)))))
                                    [:12 if i < n or num_chars == 12 else num_chars])
            nachinka += '\n'
        for i in range(n + 1 if self.size.denominator != 1 else n):
            bottom += '\\{}/'.format("".join(itertools.repeat('-', 12)))if i < n or num_chars == 12 else '\\{}|'.format(
                "".join(itertools.repeat('-', math.ceil(num_chars))))
        return top + '\n' + nachinka + bottom

    def __add__(self, other):
        new_s = sausage(self.mince)
        new_s.size = self.size + other.size
        return new_s

    def __sub__(self, other):
        new_s = sausage(self.mince)
        new_s.size = self.size - other.size
        return new_s

    def __rsub__(self, other):
        new_s = sausage(other.mince)
        new_s.size = other.size - self.size
        return new_s

    def __mul__(self, other):
        new_s = sausage(self.mince)
        new_s.size = self.size * fractions.Fraction(other)
        return new_s

    def __rmul__(self, other):
        new_s = sausage(self.mince)
        new_s.size = fractions.Fraction(other) * self.size
        return new_s

    def __truediv__(self, other):
        new_s = sausage(self.mince)
        new_s.size = self.size / fractions.Fraction(other)
        return new_s

    def __bool__(self):
        return self.size > 0
