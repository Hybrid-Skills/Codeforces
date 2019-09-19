for _ in range(int(input())):
    c, m, x = map(int, input().split())
    maxi = (c + m + x)//3

    if c >= m:
        if m <= maxi:
            print(m)
        elif m > maxi:
            print(maxi)
    else:
        if c <= maxi:
            print(c)
        else:
            print(maxi)