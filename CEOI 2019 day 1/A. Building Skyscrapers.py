n = int(input())
t = int(input())

r = []
c = []

for _ in range(n):
    rc = input().split()
    r.append(int(rc[0]))
    c.append(int(rc[1]))

for i in range(n):
    for j in range(n):
        if j == i:
            pass
        else:
            if r[j] - 1 <= r[i] <= r[j] + 1:
                if c[j] - 1 <= c[i] <= c[j] + 1:
                    break
    else:
        print('NO')
        break
else:
    print('YES')
