import random

import sympy


class Elgamal:
    p = 2243
    g = -1
    x = -1
    y = -1

    def keygen(self):
        self.g = sympy.primitive_root(self.p)
        self.x = random.randint(0, self.p - 1)
        self.y = pow(self.g, self.x, self.p)
        return (self.p, self.g, self.y), self.x

    def encrypto(self, m):
        cipher2 = []
        r = random.randint(0, self.p - 1)
        cipher1 = pow(self.g, r, self.p)
        for l in m:
            c2 = (ord(l) * pow(self.y, r, self.p)) % self.p
            cipher2.append(c2)
        return (cipher1, cipher2)

    def decrypto(self, c1, c2):
        decode = ''
        d = pow(c1, self.p - 1 - self.x, self.p)
        for c in c2:
            m = (c * d) % self.p
            decode += chr(m)
        return decode


el = Elgamal()
pk, sk = el.keygen()
c1, c2 = el.encrypto('abcs')
print(pk, sk)
print(c1)
print(c2)
dec = el.decrypto(c1, c2)
print(dec)
