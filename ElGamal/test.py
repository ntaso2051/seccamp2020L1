import random

p = 11
# while(1):
#     a = random.randint(0, p-1)
#     b = random.randint(0, p-1)
#     if((4*a*a*a % 11+27*b*b % 11) % p != 0):
#         break
# print(a, b)
a = 1
b = 2
pos=[]

for x in range(11):
    for y in range(11):
        if(y*y % 11 == (x*x*x+a*x+b) % 11):
            # print(x, y)
            pos.append((x, y))
        

def add(x1, y1, x2, y2, a):
    if(x1 == x2 and (y1+y2) % 11 == 0):
        return -1, -1
    elif(x1 == x2 and y1 == y2):
        l = (3*x1*x1+a) % 11*pow(2*y1, -1, 11)
    else:
        l = (y2-y1) % 11*pow(x2-x1, -1, 11) % 11
    x4 = (l*l % 11-x1-x2) % 11
    y4 = (l*(x1-x4) % 11-y1)%11
    return x4, y4

for p in pos:
    print("(", p[0], p[1], ")", end="")
    tx, ty=add(p[0], p[1], p[0], p[1], a)
    print("→", end="")
    print("(", tx, ty,")", end="")
    print("→", end="")
    while(1):
        if(tx==-1 and ty==-1):
            break
        tx, ty=add(tx, ty, p[0], p[1], a)
        print("(", tx, ty, ")", end="")
        print("→", end="")
    print()
        

