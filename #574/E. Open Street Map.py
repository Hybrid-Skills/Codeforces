n, m, a, b = map(int, input().split())

g, x, y, z = map(int, input().split())

gmax = (n)*m -1
answer = 0

g = [g]

for i in range(gmax):
    g.append((g[i]*(x+y))%z)

minimum = 99999999


for i in range(a):
    for j in range(b):
        minimum = min(minimum)


for i in range(1,n-a+2):
    minimum = 99999999
    for j in range(1, m-b+2):


