# (167, 5, 9) 22
# 1
# [72, 101, 108, 108, 111, 87, 111, 114, 108, 100, 33, 33]
# (127, 3, 15) 88
# 54
# [22, 112, 33, 33, 108, 16, 108, 56, 33, 87, 63, 63]
import sympy
from functools import reduce

def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        return -1
    else:
        return x % m

def chinese_remainder(a, n):
    total = 0
    prod = reduce(lambda x, y: x*y, n)
    for n_i, a_i in zip(n, a):
        b_i = prod // n_i
        total += a_i * b_i * modinv(b_i, n_i)
    return total % prod
# (64319, 13, 21858) 59517
# (15000561895574197919, 7, 10744223873724438908) 2319733465746381622
p = 15000561895574197919
phi_p = p-1
g = 7
y = 10744223873724438908

fact = []
i = 2

q = p-1
while(i*i <= phi_p):
    if(q % i == 0):
        fact.append(i)
    while(q % i == 0):
        q /= i
    i += 1
if(q!=1):
    fact.append(int(q))

print(fact)

rem = []

for f in fact:
    y2 = pow(y, int(phi_p//f), p)
    g2 = pow(g, int(phi_p//f), p)
    # print(y2, g2)
    c = 0
    while(1):
        c += 1
        if(y2 == pow(g2, c, p)):
            break
    rem.append(c)

print(rem)

ans=chinese_remainder(rem, fact)
print(ans)

# ans = sympy.ntheory.modular.crt(fact, rem)

# print(ans)
