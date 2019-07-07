q = int(input())
for _ in range(q):
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    a = list(map(int, input().split()))

    lowest = min(a)
    highest = max(a)
    if highest - lowest > 2 * k:
        print(-1)
    else:
        print(lowest + k)