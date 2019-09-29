n, m = map(int, input().split())

a = []
for i in range(n+1):
    a.append([[], []])

for i in range(m):
    x, y = map(int, input().split())
    if x > y:
        a[x][1].append(y)
        a[y][0].append(x)
    else:
        a[x][0].append(y)
        a[y][1].append(x)

q = int(input())
ans = 0

for j in range(n):
    ans += len(a[j][0]) * len(a[j][1])
print(ans)

for i in range(q):
    x = int(input())
    for j in a[x][0]:
        ans -= len(a[j][0]) * len(a[j][1])
        a[j][1].remove(x)
        a[j][0].append(x)
        ans += len(a[j][0]) * len(a[j][1])
    ans -= len(a[x][0]) * len(a[x][1])
    a[x] = [[], a[x][0] + a[x][1]]
    print(ans)
