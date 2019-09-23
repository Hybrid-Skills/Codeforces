def arr():
    return list(map(int, input().split()))


n = int(input())
a = arr()
l = [0]*(n+1)
x = []
b = a.copy()
ans = 0

b.sort(reverse=True)

for i in a:
    x.append([i,0])

for i in range(n):
    x[x.index([b[i], 0])] = [b[i], i+1]

c = []

for i in x:
    c.append(i[1])

for i in range(n):
    ans += x[i][0]*(x[i][1] - 1) + 1

print(ans)

for i in range(n):
    l[x[i][1]] = i+1

print(' '.join(map(str,l[1:])))