n = int(input())
a = list(map(int, input().split()))
b = {}
for i in range(n):
    try:
        b[a[i]].append(i)
    except KeyError:
        b[a[i]] = [i]

c = None
d = None

for i in range(n):
    if len(b[a[i]]) > 1:
        c = [b[i][0], b[i][-2]]
        d = [b[i][1], b[i][-1]]
        break

if c:
    for i in range(n):
        if len(b[a[i]]) > 1:
            count = 0
            for j in range(len(b[a[i]])):
                if c[0] <= b[a[i]][j] <= c[1]:
                    pass
                else:
                    count += 1
            if count >= 1:
