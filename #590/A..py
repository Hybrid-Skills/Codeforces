for _ in range(int(input())):
    n = int(input())

    a = list(map(int, input().split()))

    s = sum(a)

    print(s//n + 1 if s%n != 0 else s//n)