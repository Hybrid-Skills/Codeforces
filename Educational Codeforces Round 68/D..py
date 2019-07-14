t = int(input())

for _ in range(t):
    n, k = [int(i) for i in input().split()]
    if k % 3 != 0 or n < k:
        if n % 3 == 0:
            print('Bob')
        else:
            print('Alice')

    else:
        if n % (k+1) == 0:
            print('Bob')
        elif (n% (k+1)) % 3 == 0 and (n% (k+1)) != k:
            print('Bob')
        else:
            print('Alice')
