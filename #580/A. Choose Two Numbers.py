n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        if a[i] + b[j] not in a and a[i] + b[j] not in b:
            print(a[i], b[j])
            break
    else:
        continue
    break