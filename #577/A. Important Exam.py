n, m = map(int, input().split())

s = []
ans = []

for _ in range(n):
    s.append(input())

for i in range(m):
    a = [0,0,0,0,0]
    for j in range(n):
        if s[j][i] == 'A':
            a[0] += 1
        elif s[j][i] == 'B':
            a[1] += 1
        elif s[j][i] == 'C':
            a[2] += 1
        elif s[j][i] == 'D':
            a[3] += 1
        else:
            a[4] += 1
    ans.append(max(a))

q = list(map(int, input().split()))

total = 0

for i in range(m):
    total += q[i]*ans[i]

print(total)