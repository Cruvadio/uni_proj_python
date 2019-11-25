import fractions
import itertools
import math
class sausage:
    def __init__(self, *args):
        self.mince = "pork!"
        self.size = fractions.Fraction(1).
        if len(args) > 0:
            self.mince = args[0]
        if len(args) > 1:
            self.size = args[1]

    def __str__(self):
        n = self.size.__floor__()
        num_chars = 12 * abs(float(self.size) - n)
        for i in range(n + 1):
            string = '/{}\\'.format(itertools.repeat('-', 12)) if i < n or num_chars == 12 else '/{}|'.format(itertools.repeat('-', num_chars))
            string += '|{}|'.format(itertools.repeat(self.mince, math.ceil(12/self.mince if i < n or num_chars == 12 else 12))) if