import random

import sympy


class Elgamal:
    p = -1
    g = -1
    x = -1
    y = -1

    def __is_even(self, n):
        if n % 2 == 0:
            return True
        else:
            return False

    def __is_prime(self, n):
        if n == 2:
            return True
        if n <= 1 or self.__is_even(n):
            return False

        d = (n - 1) >> 1
        while self.__is_even(n):
            d >>= 1

        for i in range(100):
            a = random.randint(1, n-1)
            t = d
            y = pow(a, t, n)

            while t != n - 1 and y != 1 and y != n - 1:
                y = pow(y, 2, n)
                t <<= 1

            if y != n - 1 and self.__is_even(t):
                return False

        return True

    def __get_prime(self, k):
        if(1 << k <= 1):
            return -1

        while(True):
            q = random.randint(1 << (k-2), 1 << (k-1))
            if(self.__is_even(q)):
                q += 1
            if(self.__is_prime(q)):
                break

        return q

    def keygen(self, k):
        c = 1
        _p = 1
        _p=self.__get_prime(k)
        self.p = _p
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
pk, sk = el.keygen(8)
c1, c2 = el.encrypto('HelloWorld!!')
print(pk, sk)
print(c1)
print(c2)
dec = el.decrypto(c1, c2)
print(dec)
