for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))

    if n < 3:
        print('YES')

    else:
        dif1 = p[1] - p[0]
        dif2 = p[2] - p[1]

        if dif1 in [-1, 1]:
            for i in range(n-1):
                if dif1 == 1:
                    if p[i+1] - p[i] != dif1 and p[i+1] != 1:
                        print('NO')
                        break
                else:
                    if p[i+1] - p[i] != dif1 and p[i] != 1:
                        print('NO')
                        break
            else:
                print('YES')
        elif dif2 in [-1, 1]:
            for i in range(1, n-1):
                if p[i+1] - p[i] != dif2:
                    print('NO')
                    break
            else:
                print('YES')
        else:
            print('NO')
