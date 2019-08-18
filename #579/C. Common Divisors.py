import math
n = int(input())
ans = 0
a = list(map(int, input().split()))
if n == 1:
    x = a[0]

else:
    x = math.gcd(a[1], a[0])

    for i in range(n):
        x = math.gcd(x, a[i])

for i in range(1, int(math.sqrt(x)) + 1):
    if x%i == 0:
        if x/i == i:
            ans += 1
        else:
            ans += 2

print(ans)
