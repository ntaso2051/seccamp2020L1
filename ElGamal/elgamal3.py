import random

import sympy


class Elgamal:
    p = -1
    q = -1
    # g = -1
    x = -1
    # y = -1
    # G = -1
    a = -1
    b = -1
    pos = (1, 1)
    q2 = -1
    Y = (1, 1)
    poss = []

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
            r = random.randint(1, n-1)
            t = d
            y = pow(r, t, n)

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
            _q = random.randint(1 << (k-2), 1 << (k-1))
            if(self.__is_even(_q)):
                _q += 1
            if(self.__is_prime(_q)):
                break

        return _q

    def __ellipticAdd(self, p1, p2):
        l = -1
        if(p1[0] == -1):
            return p2
        elif(p2[0] == -1):
            return p1
        elif(p1[0] == p2[0] and (p1[1]+p2[1]) % self.p == 0):
            return (-1, -1)
        elif(p1[0] == p2[0] and p1[1] == p2[1]):
            l = (3*p1[0]*p1[0]+self.a) % self.p*pow(2*p1[1], -1, self.p)
        else:
            l = (p2[1]-p1[1]) % self.p*pow(p2[0]-p1[0], -1, self.p) % self.p
        x4 = (l*l % self.p-p1[0]-p2[0]) % self.p
        y4 = (l*(p1[0]-x4) % self.p-p1[1]) % self.p
        return (x4, y4)

    def __initPoss(self):
        s = [0]*self.p
        for j in range((self.p-1)//2+1):
            s[j*j % self.p] = j
        for x in range(self.p):
            z = (x*x*x % self.p+self.a*x % self.p+self.b) % self.p
            c = (self.p-1)//2
            if(pow(z, c, self.p) == 1):
                # print(x)
                self.poss.append((x, s[z]))
                self.poss.append((x, self.p-s[z]))
        # return poss[random.randint(0, len(poss)-1)]

    def __getOrder(self):
        _q = 0
        while(1):
            self.pos = self.poss[random.randint(0, len(self.poss)-1)]
            _tpos = self.__ellipticAdd(self.pos, self.pos)
            _q += 1
            while(1):
                if(_tpos[0] == -1 and _tpos[1] == -1):
                    break
                _tpos = self.__ellipticAdd(_tpos, self.pos)
                _q += 1
            if(_q > self.p//2):
                break
        self.q2 = _q

    def keygen(self, k):
        c = 1
        _p = 1
        while(1):
            _q = self.__get_prime(k)
            _p = 2 * _q * c + 1
            if (self.__is_prime(_p)):
                self.q = _q
                break
        self.p = _p
        # self.g = sympy.primitive_root(self.p)
        # _G = pow(self.g, 2, self.p)
        # \alpha = g^{\frac{p-1}{q}} = g^{\frac{2q+1-1}{q}} = g^2
        # self.G = pow(_G, random.randint(0, self.q-1), self.q)
        # self.x = random.randint(0, self.q2 - 1)
        # self.y = pow(self.g, self.x, self.q)
        while(1):
            self.a = random.randint(1, self.p-1)
            self.b = random.randint(1, self.p-1)
            if(4*self.a*self.a*self.a+27*self.b*self.b != 0):
                break
        self.__initPoss()
        self.__getOrder()
        self.x = random.randint(1, self.q2-1)
        self.Y = self.pos
        for i in range(self.x):
            self.Y = self.__ellipticAdd(self.Y, self.pos)
        return (self.p, self.a, self.b, self.pos, self.Y), self.x

    def encrypto(self, m):
        cipher2 = []
        r = random.randint(0, self.q2 - 1)
        _tpos = self.pos
        _ppos = self.Y
        for i in range(r):
            _tpos = self.__ellipticAdd(_tpos, self.pos)
            _ppos = self.__ellipticAdd(_ppos, self.Y)
        cipher1 = _tpos
        for l in m:
            c2 = ((self.poss[ord(l)][0] + _ppos[0]) %
                  self.p, (self.poss[ord(l)][1]+_ppos[1]) % self.p)
            cipher2.append(c2)
        return (cipher1, cipher2)

    def decrypto(self, c1, c2):
        decode = ''
        m = 39
        xc1 = c1
        for i in range(self.x):
            xc1 = self.__ellipticAdd(xc1, c1)
        for c in c2:
            for i in range(len(self.poss)):
                if((c[0]-xc1[0]) % self.p == self.poss[i][0] and (c[1]-xc1[1]) % self.p == self.poss[i][1]):
                    m = i
                    break
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
