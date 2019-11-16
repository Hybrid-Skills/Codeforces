m, n = map(int, input().split())
mod = 1000000007


def pow1(a,b):
    x = 1
    for i in range(b):
        x = (x * a) % mod
    return x


def power(x, y):
    if y == 0:
        return 1

    temp = power(x, int(y // 2))

    if y % 2 == 0:
        return temp * temp % mod
    else:
        if y > 0:
            return x * temp * temp % mod
        else:
            return (temp * temp) / x


ans = power(power(2, n) - 1, m) % mod

print(ans)