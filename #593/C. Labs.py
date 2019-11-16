n = int(input())

ans = [[] for i in range(n)]

for i in range(n):
    for j in range(n):
        if j%2 == 1:
            ans[i].append((j+1)*n - i)
        else:
            ans[i].append(j*n + i + 1)

for i in range(n):
    print(' '.join(map(str, ans[i])))
