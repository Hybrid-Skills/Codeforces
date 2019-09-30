n, m = map(int, input().split())
v = [2 for i in range(n)]
x = [False for i in range(n)]
gr = [[] for j in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    gr[x-1].append(y-1)
    gr[y-1].append(x-1)

for i in gr:
    if len(i) < 2:
        print(-1)
        quit()
# print(gr)

for i in gr[0]:
    x[i] = True

for i in range(n):
    if not x[i]:
        v[i] = 0

for i in gr[gr[0][0]]:
    if x[i]:
        v[i] = 1

v1 = 0
v0 = 0

for i in v:
    if i == 0:
        v0 += 1
    elif i == 1:
        v1 += 1

v2 = n - v0 - v1

if v1 == 0 or v2 == 0 or v0 == 0:
    print(-1)
    quit()

for i in range(n):
    if (v[i] == 0 and len(gr[i]) != v1 + v2) or \
            (v[i] == 1 and len(gr[i]) != v0+ v2) or \
            (v[i] == 2 and len(gr[i]) != v1 + v0):
        print(-1)
        quit()
#
# for i in range(n):
#     for j in gr[i]:
#         if v[i] == v[j]:
#             print(-1)
#             quit()

for i in v:
    print(i+1, end=' ')
