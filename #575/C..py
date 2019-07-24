for _ in range(int(input())):
    n = int(input())
    robots = []
    ans_limit = [-100000, 100000, 100000, -100000]
    for i in range(n):
        robots.append([int(j) for j in input().split()])
    for i in robots:
        if i[2] == 0 and i[0] > ans_limit[0]:
            ans_limit[0] = i[0]
        if i[3] == 0 and i[1] < ans_limit[1]:
            ans_limit[1] = i[1]
        if i[4] == 0 and i[0] < ans_limit[2]:
            ans_limit[2] = i[0]
        if i[5] == 0 and i[1] > ans_limit[3]:
            ans_limit[3] = i[1]
        # print(ans_limit)

    if ans_limit[0] > ans_limit[2]:
        print(0)
    elif ans_limit[1] < ans_limit[3]:
        print(0)
    else:
        print(1, ans_limit[0], ans_limit[3])