n, k = map(int, input().split())

s = input()

ans = 0

i = 0

l = [0]*n

for i in range(k, n):
    if s[i] == '1':
        if l[min(n-1, i+k)] == 0:
            for j in range(max(0, i-k), min(n, i+k+1)):
                l[j] = 1
            ans += i + 1

for i in range(k-1,-1,-1):
    if s[i] == '1':
        if l[0] == 0:
            for j in range(k):
                l[j] = 1
    # elif s[i] == '1' and i < k:
    #     if '1' not in s[i+1:k+1]:
    #         if l[min(n - 1, i + k)] == 0:
    #             for j in range(max(0, i - k), min(n, i + k + 1)):
    #                 l[j] = 1
    #             ans += i + 1

print(l)

for i in range(n):
    if l[i] == 0:
        ans += i+1

print(ans)