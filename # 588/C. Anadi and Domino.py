n, m = map(int, input().split())

a = []
for i in range(n+1):
    a.append([])

for i in range(m):
    x, y = map(int, input().split())

    a[x].append(y)
    a[y].append(x)

a.sort(key=lambda b: len(b), reverse=True)

for i in range(len(a)):
    if not a[i]:
        break
    else:
        for j in a[i]:
            pass
