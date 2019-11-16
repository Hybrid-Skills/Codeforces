def arr():
    return list(map(int, input().split()))


for _ in range(int(input())):
    a, b, c = map(int, input().split())

    ans = 0

    if c//2 <= b:
        ans += 3 * (c//2)
        b -= c//2

        ans += 3 * min(a, b//2)

    else:
        ans += 3 * b

    print(ans)
