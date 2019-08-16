n, k = map(int, input().split())

a = []
for i in range(n):
    a.append(input())

b = zip(*a)

for i in range(n-k):
    for j in range(n-k):
        a1 = []
        a1 += a
        b1 = []
        b1 += b


