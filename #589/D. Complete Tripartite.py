n, m = map(int, input().split())
v = [0 for i in range(n)]
gr = [[] for i in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    gr[x].append(y)
    gr[y].append(x)

v[0] = 1
x = gr[0].pop()
v[x] = 2
y = gr[x].pop()
i = 2

while True:
    if y in gr[x]:
