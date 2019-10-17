from collections import defaultdict

n, k = map(int, input().split())

id = list(map(int, input().split()))
cnt = 0

a = [None for i in range(k)]
d = defaultdict(int)

for i in id:
    if d[i] == 0:
        d[a[-1]] = 0
        a = [i] + a[:-1]
        d[i] = 1
        cnt += 1
    # print(a)

print(min(cnt, k))

for i in a:
    if i is None:
        break
    print(i, end=' ')
