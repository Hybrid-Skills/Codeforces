for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    rgb = 'RGB'
    least1 = 20000000
    for j in range(3):
        ans = [0 for i in range(n)]
        for i in range(n):
            if s[i] != rgb[(i+j) % 3]:
                ans[i] = 1
        least = sum(ans[:k])
        total = sum(ans[:k])
        for i in range(k, n):
            total = total + ans[i] - ans[i-k]
            least = min(least, total)
            # print(least , total)
        least1 = min(least1, least)
        # print(least1)

    print(least1)
