n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

a[0] += 1

ans = 0

for i in range(1, n):
    if a[i] == a[i-1] and a[i] != 1:
        a[i] -= 1
        ans += 1
    elif a[i] == a[i-1] - 1:
        ans += 1
    elif a[i] < a[i-1] - 1:
        ans += 1
        a[i] += 1
    elif a[i] > a[i-1]:
        a[i] -= 1

print(ans + 1)