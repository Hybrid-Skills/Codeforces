t = int(input())

for _ in range(t):
    x = int(input(), 2)
    y = int(input(), 2)

    if x % 2 == 1 and y % 2 == 1:
        print(0)

    else:
        k = 0
        if y % 2 == 1 and x % 2 == 0:
            k += 1
            y = y * 2
        while x != 1:
            if x % 2 == 1 and y % 2 == 1:
                break
            x = x//2
            y = y//2
            if y % 2 == 1 and x % 2 == 0:
                k += 1
                y = y*2

        print(k)
