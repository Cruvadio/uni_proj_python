from itertools import *


def chainslice (begin, end, seq0, *seqs):
    if seqs:
        for seq in seqs:
            seq0 = chain(seq0, seq)
    return islice(seq0, begin, end)
