n = int(input())

a = list(map(int, input().split()))

if sum(a) % 2 != 0:
    print('NO')

else:
    a.sort(reverse=True)
    if a[0] > sum(a[1:]):
        print('NO')
    else:
        print('YES')
