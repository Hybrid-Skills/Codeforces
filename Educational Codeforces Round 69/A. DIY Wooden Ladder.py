for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    a.sort()
    rungs = n - 2
    b = [a[n-2], a[n-1]]

    # while rungs >= 0:
    #     if min(b) >= rungs + 1:
    #         print(rungs)
    #         break
    #     else:
    #         if b[0] <= b[1]:
    #             b[0] += a[rungs - 1]
    #         else:
    #             b[1] += a[rungs - 1]
    #
    #         rungs -= 1

    print(min(min(b) - 1 , n - 2))
