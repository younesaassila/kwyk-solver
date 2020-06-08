import scipy.stats

(u, o) = (0, 1)

class Normale(object):
    def __init__(self, u, o):
        self.norm = scipy.stats.norm(u, o)

    def p_X_inf(self, a): return self.norm.cdf(a)
    def p_X_sup(self, a): return 1 - self.p_X_inf(a)  # return norm.sf(a)

    def p_X_btw(self, a, b):
        if a > b:
            # si dans le mauvais sens, on les retourne
            return self.p_X_btw(b, a)
        if a == b:
            return 0.0
        return 1 - self.p_X_inf(a) - self.p_X_sup(b)


def test_centreeReduite(a, b):
    centreeReduite = Normale(u, o)
    p = centreeReduite.p_X_btw(a, b)
    print(p)