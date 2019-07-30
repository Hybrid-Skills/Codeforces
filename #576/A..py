n, x, y = map(int, input().split())

a = [int(i) for i in input().split()]

up = 0
down = 0
reach = False
ans = x

for i in range(n-y):
    # print('i', i)
    if a[max(i-x, 0):i+y+1].index(min(a[max(i-x, 0):i+y+1])) == i - max(0, i-x):
        print(i+1)
        break


else:
    j = n-y
    while j < n:
        # print('j', j)
        if a[max(0, j-x):].index(min(a[max(0, j-x):])) == j - max(0, j-x):
            print(j+1)
            break
        j += 1