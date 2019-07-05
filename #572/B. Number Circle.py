n = int(input())
a = list(map(int, input().split()))

high = max(a)
a.remove(high)
high1 = max(a)
a.remove(high1)
high2 = max(a)


if high >= high1 + high2:
    print('NO')

else:
    a.sort()
    a.append(high)
    a.append(high1)
    print('YES')
    for i in a:
        print(i, end=' ')
