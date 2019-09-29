x, n = map(int, input().split())
ans = 1


def power(m, y):
    res = 1
    while y > 0:
        if (y & 1) == 1:
            res = (res * m) % 1000000007

        y = y >> 1
        m = m * m % 1000000007

    return res


# To find prime
arr = []
f = x
cnt = 2
while cnt*cnt <= f:
    while f % cnt == 0:
        arr.append(cnt)
        f = f//cnt
    cnt += 1
arr = set(arr)
arr = list(arr)

if f != 1:
    arr.append(f)

for i in range(len(arr)):
    j = arr[i]
    while j <= n:
        ans = ans * power(arr[i], n//j) % 1000000007
        j = j*arr[i]

print(ans)
