def arr():
    return list(map(int, input().split()))


def gcd(a,b):
    while (b):
        a, b = b, a % b

    return a


n = int(input())
a = arr()
b = []
x = max(a)

for i in a:
    if x-i != 0:
        b.append(x-i)

ans = b[0]

for i in range(len(b)):
    ans = gcd(ans, b[i])

y = sum(b) // ans

print(y, ans)