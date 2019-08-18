n = int(input())

if n%2 == 0:
    print('NO')

else:
    print('YES')

    arr = [0 for i in range(2 * n)]

    j = 1
    i = 0
    arr[i] = j

    for _ in range(n - 1):
        j += 1
        i = (i+n)%(2*n)
        arr[i] = j
        j += 1
        i += 1
        arr[i] = j

    arr[(i+n)%(2*n)] = j+1

    print(' '.join(list(map(str, arr))))