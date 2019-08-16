for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = [int(i) for i in input().split()]

    for i in range(n-1):
        if -k <= a[i] - a[i+1]:
            m += min(k + a[i] - a[i+1], a[i])
        elif -k - m <= a[i] - a[i+1]:
            m += a[i] - a[i+1] + k
        else:
            print('NO')
            break
    else:
        print('YES')