import collections
def checkhash (seq, f, mod):
    return (lambda x : (max(x.values()), min(x.values()))) (collections.Counter([f(s) % mod for s in seq]))

