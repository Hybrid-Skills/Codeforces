for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    lowest = a[-1]
    bad = 0

    for i in range(1,n):
        if a[-i-1] > lowest:
            bad += 1
        else:
            lowest = a[-i-1]

    print(bad)