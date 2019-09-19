for _ in range(int(input())):
    a, b = map(int, input().split())
    s = input()

    x = 0
    q = []
    a1 = []
    b1 = []

    for i in s:
        if i == '.':
            x += 1
        elif x >= 1:
            if x >= a:
                a1.append(x)
            if x >= b:
                b1.append(x)
            q.append(x)
            x = 0

