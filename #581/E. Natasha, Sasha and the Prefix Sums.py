n, m = map(int, input().split())


def comb(a, b):
    x = fact[a] // (fact[b] * fact[a-b])
    return x


fact = [None for i in range(2001)]
fact[0] = 1
j = 1
for i in range(1,2001):
    j = j * i
    fact[i] = j

total = 0

for i in range(min(n+1, m+1)):
    n_sum = comb(n, i)
    m_sum = comb(m, i)
    mult = 0
    for j in range(i+1):
        mult += (comb(n, i-j))*(comb(m, j))
    total += (n-i)*mult
    print(total)

print(total % 998244853)