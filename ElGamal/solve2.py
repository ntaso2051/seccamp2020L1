import math


def ellipticAdd(p1, p2):
    l = -1
    if(p1[0] == -1):
        return p2
    elif(p2[0] == -1):
        return p1
    elif(p1[0] == p2[0] and (p1[1]+p2[1]) % p == 0):
        return (-1, -1)
    elif(p1[0] == p2[0] and p1[1] == p2[1]):
        l = (3*p1[0]*p1[0]+a) % p*pow(2*p1[1], -1, p)
    else:
        l = (p2[1]-p1[1]) % p*pow(p2[0]-p1[0], -1, p) % p
    x4 = (l*l % p-p1[0]-p2[0]) % p
    y4 = (l*(p1[0]-x4) % p-p1[1]) % p
    return (x4, y4)


def baby_step_giant_step(q, P, Q):
    m = int(math.sqrt(q))+1

    baby = []
    b = Q
    for j in range(m):
        baby.append(b)
        b = ellipticAdd(b, (P[0], (p-P[1]) % p))

    giant = P
    for i in range(m-1):
        giant = ellipticAdd(giant, P)
    for i in range(1, m):
        # for j in range(len(baby)):
        if giant in baby:
            d = i*m+baby.index(giant)-1
            return d
        else:
            tP = P
            for k in range(m-1):
                tP = ellipticAdd(tP, P)
            giant = ellipticAdd(giant, tP)
    return -1


p = 61703
a = 11435
b = 48476
q2 = 62020
P = (37083, 34627)
Q = (21423, 25071)


d = baby_step_giant_step(q2, P, Q)
print(d)


# (self.p, self.a, self.b, self.pos, self.Y, self.q2), self.x
# (167, 21, 158, (15, 72), (30, 20), 158) 57
# (167, 16, 35, (74, 74), (84, 8), 153) 37
# (61703, 11435, 48476, (37083, 34627), (21423, 25071), 62020) 23443
