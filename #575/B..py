for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = []

    for i in range(n):
        if a[i] % 2 == 1:
            ans.append(i+1)

    if len(ans) >= k and len(ans) % 2 == k % 2:
        print('YES')
        for i in ans[:k-1]:
            print(i, end=' ')
        print(n)
    else:
        print('NO')
