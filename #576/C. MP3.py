n, I = map(int, input().split())

a = [int(i) for i in input().split()]

kn = len(set(a))

kp = int(2 ** (I * 8 / n))

red = max(kn - kp, 0)

a.sort()
ans = 0
bottom = 0
top = 0

while red > 0:
    if bottom == 0:
        for i in range(n-1):
            if a[i] != a[i+1]:
                bottom = i
                break
    if top == 0:
        for i in range(1, n):
            if a[-i-1] != a[-i]:
                top = i
                break
    if top > bottom:
        a = a[bottom+1:]
        ans += bottom + 1
        bottom = 0
    else:
        a = a[:-top]
        ans += top
        top = 0
    red -= 1

print(ans)