def function(n,a,b):
    for i in range(0,n):
        if a[i] != b[i]:
            l = i
            x = b[i] - a[i]
            break
    else:
        return 'YES'

    if x < 0:
        return 'NO'

    for i in range(l, n):
        if a[i] != b[i] - x and a[i] != b[i]:
            return 'NO'
        elif a[i] == b[i]:
            for j in range(i,n):
                if a[j] != b[j]:
                    return 'NO'
            else:
                return 'YES'
    else:
        return 'YES'


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(function(n,a,b))