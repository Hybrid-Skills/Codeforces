for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()

    x = [[i for i in a]] + [[j for j in b]]

    d = 1
    i = 0
    j = 0

    while True:
        if x[i][j] == '1' or x[i][j] == '2':
            if d == 1:
                if j == n-1 and i == 1:
                    print('YES')
                    break
                elif j == n-1:
                    print('NO')
                    break
                else:
                    j += 1

            else:
                print('NO')
                break

        elif x[i][j] in '3456':
            if d == 1:
                if i == 0:
                    i = 1
                    d = 2
                elif i == 1:
                    i = 0
                    d = -2
            elif d == 2 or d == -2:
                if j == n-1:
                    if i == 0:
                        print('NO')
                    else:
                        print('YES')
                    break
                else:
                    d = 1
                    j += 1
        # print(i,j)
