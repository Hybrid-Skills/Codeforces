for _ in range(int(input())):
    n = int(input())
    planks = []

    for i in range(n):
        planks.append([int(j) for j in input().split()])

    d1 = [0]
    d2 = [0]

    for i in range(1, n):
        if planks[i-1][0] == planks[i][0]:
            d1.append(d1[-1] + planks[i][2])
