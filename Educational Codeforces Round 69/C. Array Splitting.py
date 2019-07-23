n, k = map(int, input().split())

a = [int(i) for i in input().split()]

d = []

for i in range(n-1):
    d.append(a[i+1] - a[i])

d.sort()

print(sum(d[:n - k]))
