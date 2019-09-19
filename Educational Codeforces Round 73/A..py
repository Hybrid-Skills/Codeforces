def arr():
    return list(map(int, input().split()))


for _ in range(int(input())):
    n = int(input())
    s = arr()

    x = 2048
    y = 1

    while y>0 and x>=1:
        if x in s:
            y -= 1
            s.remove(x)
            if y == 0:
                print('YES')
                break
        else:
            x //= 2
            y = y*2
        # print(x, y, s)
    else:
        print('NO')