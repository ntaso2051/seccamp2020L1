import random

import sympy


class Elgamal:
    p = 7

    def keygen(self):
        g = sympy.primitive_root(self.p)
        x = random.randint(0, self.p - 1)
        y = pow(g, x, self.p)
        return (self.p, g, y), x


el = Elgamal()
print(el.keygen())
