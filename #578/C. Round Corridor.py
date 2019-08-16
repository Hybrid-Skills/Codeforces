import math

n, m, q = map(int, input().split())

a = [list(map(int, input().split())) for i in range(q)]

gcd = math.gcd(n, m)

kn = n // gcd
km = m // gcd

for i in range(q):
    if a[i][0] == 1:
        x = a[i][1] // kn
        if a[i][1] % kn != 0:
            x += 1
    else:
        x = a[i][1] // km
        if a[i][1] % km != 0:
            x += 1

    if a[i][2] == 1:
        y = a[i][3] // kn
        if a[i][3] % kn != 0:
            y += 1
    else:
        y = a[i][3] // km
        if a[i][3] % km != 0:
            y += 1
    if x == y:
        print('YES')
    else:
        print('NO')
