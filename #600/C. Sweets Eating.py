n, m = map(int, input().split())

a = list(map(int, input().split()))
a.sort()

# for k in range(1, n+1):
#     d = k//m
#     if k % m != 0:
#         d += 1
#     sugar = 0
#     for i in range(d):
#         sugar += (i+1)*(sum(a[max(0,k-(i+1)*m): k - i*m]))
#
#     print(sugar, end=' ')
ans = [0 for i in range(n)]

# for i in range(n):
# #     for j in range(i, n):
# #         ans[j] += a[i]*(((j-i)//m) + 1)
# #
# # print(' '.join(map(str, ans)))

ans[0] = a[0]

for i in range(1,n):
    ans[i] = ans[i-1] + a[i]

for i in range(n):
    if i >= m:
        ans[i] += ans[i-m]
        print(ans[i], end= ' ')
    else:
        print(ans[i], end = ' ')