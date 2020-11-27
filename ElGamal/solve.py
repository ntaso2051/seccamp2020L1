import math
from functools import reduce


def init_eratosthenes(n):
    mx = int(math.sqrt(n))+1
    minf[0] = 0
    minf[1] = 0
    for i in range(2, mx):
        if(minf[i] < i):
            continue
        for j in range(i*i, n+1, i):
            if(minf[j] == j):
                minf[j] = i


def prime_factrize(n):
    num = n
    cnt = 0
    p = minf[num]
    if num <= 1:
        return
    while(num % p == 0):
        # print(num)
        num = int(num//p)
        cnt += 1
    prime.append(p)
    prime_factrize(num)


def egcd(m, n):
    if n > 0:
        y, x, d = egcd(n, m % n)
        return (x, y-int(m//n)*x, d)
    else:
        return 1, 0, m


def modinv(a, m):
    (inv, q, gcd_val) = egcd(a, m)
    return inv % m


def chinese_remainder(Q, X):
    r = 0
    M = 1
    for i in range(0, len(X)):
        x, y, d = egcd(M, Q[i])
        if (X[i]-r) % d != 0:
            return 0
        # print(d)
        if(Q[i]!=0):
            tmp = (int((X[i]-r)//d)*x) % (int(Q[i]//d))
            r += M*tmp
            M *= int(Q[i]//d)
    return r % M


def baby_step_giant_step(g, y, p, q):
    m = int(math.sqrt(q))+1

    baby = {}
    b = 1
    for j in range(m):
        baby[b] = j
        b = (b * g) % p

    gm = pow(int(modinv(int(g), p)), m, int(p))
    giant = y
    for i in range(m):
        if giant in baby:
            x = i*m + baby[giant]
            return x
        else:
            giant = (giant * gm) % p
    return -1


def pohlig_hellman(p, g, y, Q):
    print("[+] Q:", Q)
    X = []
    for q in Q:
        x = baby_step_giant_step(
            pow(g, int((p-1)//q), p), pow(y, int((p-1)//q), p), p, int(q))
        X.append(x)
    print("[+] X:", X)
    x = chinese_remainder(Q, X)
    return x

# (49103, 5, 28097) 9244
p = 49103
g = 5
y = 28097
prime = []
minf = list(range(0, p))
# print(minf)
init_eratosthenes(p-1)
prime_factrize(p-1)
# print(minf)
x = pohlig_hellman(p, g, y, prime)
print(x)

# (167, 5, 63) 140
