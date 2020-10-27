# p = 0x303135
# q = 0x313537
p = 0x303030
q = 0x303030

ans = 0x9436faf8b63
print(hex(ans))

keta = 0
p = p + (1 << (8 * (keta + 1)))
print(hex(p))

while (1):
    if (keta == 3):
        break
    for i in range(10):
        tp = p + (i << (8 * (keta)))
        for j in range(10):
            tq = q + (j << (8 * (keta)))
            if (tp * tq % (1 << (8 * (keta+1))) == ans % (1 << (8 * (keta+1)))):
                p = tp
                q = tq
                keta += 1


print(hex(p % (1 << (8*2))))
print(hex(p), hex(q))
