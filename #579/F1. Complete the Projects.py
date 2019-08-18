n, r = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

b = []

for i in a:
    if i[1] >= 0:
        b.append(i)
        a.remove(i)

b.sort(key= lambda a: a[0])
a.sort(key = lambda b: b[0])
a.reverse()

# print(b)
# print(a)

for i in b:
    if i[0] > r:
        print('NO')
        break
    else:
        r += i[1]
else:
    for i in a:
        if i[0] > r:
            print('NO')
            break
        else:
            r += i[1]
    else:
        print('YES')
