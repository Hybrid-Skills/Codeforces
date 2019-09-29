def arr():
    return list(map(int, input().split()))

a = arr()
a.sort()

if a[0] + a[3] == a[1] + a[2]:
    print('YES')
elif a[3] == a[0] + a[1] + a[2]:
    print('YES')
else:
    print('NO')