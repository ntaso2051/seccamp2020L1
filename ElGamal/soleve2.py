import math

def ellipticAdd(p1, p2):
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

def baby_step_giant_step(q, P, Q):
    m=int(math.sqrt(q))+1

    baby=[]
    b=Q
    for j in range(m):
        baby.append(b)
        b=ellipticAdd(b, P)
    
    giant=P
    for i in range(m):
        giant=ellipticAdd(giant, P)
    for i in range(1, m):
        