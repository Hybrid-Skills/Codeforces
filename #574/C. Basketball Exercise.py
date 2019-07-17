n = int(input())

h1 = [int(i) for i in input().split()]

h2 = [int(i) for i in input().split()]

dp1 = [h1[0]]
dp2 = [h2[0]]

if n >= 2:
    dp1.append(h2[0] + h1[1])
    dp2.append(h1[0] + h2[1])

for i in range(2, n):
    dp1.append(max(dp2[i-1], dp2[i-2]) + h1[i])
    dp2.append(max(dp1[i-2], dp1[i-1]) + h2[i])

print(max(dp1[n-1], dp2[n-1]))
