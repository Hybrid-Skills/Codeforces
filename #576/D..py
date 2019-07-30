n = int(input())

a = [int(i) for i in input().split()]

q = int(input())

for _ in range(q):
    ans = input().split()
    if ans[0] == '1':
        a[int(ans[1])-1] = int(ans[2])
    else:
        for i in range(n):
            a[i] = max(a[i], int(ans[1]))

print(' '.join(map(str, a)))