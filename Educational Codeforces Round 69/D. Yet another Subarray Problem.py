import math

n, m, k = map(int, input().split())

a = [int(i)for i in input().split()]

i = 0
j = 0

cost = 0

while i <= n-1 and j <= n-1:
    temp_cost = sum(a[i:j+1]) - math.ceil((j - i + 1) / m) * k

    if temp_cost <= 0:
        i = j+1
        j += 1
    else:
        if temp_cost > cost:
            cost = temp_cost
        j += 1

print(cost)