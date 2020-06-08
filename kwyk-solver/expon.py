import scipy.stats

parametre = 1

class exponentielle (object):
    def __init__(self, para):
        self.expon = scipy.stats.expon(para)

    def p_X_inf(self,a) : return self.expon.cdf(a)
    def p_X_sup(self,a) : return 1 - self.p_X_inf(a)
    def p_X_btw(self,a,b) :
        if a > b : return self.p_X_btw(b,a) #si dans le mauvais sens, on les retourne
        if a == b: return 0.0
        return 1 - self.p_X_inf(a) - self.p_X_sup(b)

def test_exponentielle(a,b):
    expo = exponentielle(parametre)
    p = expo.p_X_btw(a,b)
    print(p)

test_exponentielle(0,1)