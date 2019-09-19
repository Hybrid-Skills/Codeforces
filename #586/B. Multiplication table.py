import math

n = int(input())

a = []

for i in range(n):
    a.append([int(i) for i in input().split()])

x2 = (a[0][1] * a[0][2]) // a[1][2]

x = int(math.sqrt(x2))

z = [x]

for i in range(1,n):
    z.append(a[0][i]//x)

for i in range(n):
    print(z[i], end=' ')