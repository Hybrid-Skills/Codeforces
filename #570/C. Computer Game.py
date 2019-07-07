q = int(input())

for _ in range(q):
    knab = input().split()
    k = int(knab[0])
    n = int(knab[1])
    a = int(knab[2])
    b = int(knab[3])
    if k <= n * b:
        print(-1)
    else:
        print(min((k - 1 - (n * b)) // (a - b), n))