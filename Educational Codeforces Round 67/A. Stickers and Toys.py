t = int(input())

for _ in range(t):
    n, s, t = [int(i) for i in input().split()]

    common = s + t - n
    print(max(s, t) - common + 1)