p = 11
# while(1):
#     a = random.randint(0, p-1)
#     b = random.randint(0, p-1)
#     if((4*a*a*a % 11+27*b*b % 11) % p != 0):
#         break
# print(a, b)
a = 1
b = 2
pos = []

# for x in range(11):
#     for y in range(11):
#         if(y*y % 11 == (x*x*x+a*x+b) % 11):
#             # print(x, y)
#             pos.append((x, y))

s = [0]*11
for j in range((p-1)//2+1):
    s[j*j % p] = j
print(s)

for x in range(p):
    z = (x*x*x % 11+a*x % 11+b) % 11
    c = int((p-1)/2)
    if(pow(z, c, p) == 1):
        # print(x)
        print(x, s[z])
        print(x, p-s[z])
