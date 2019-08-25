n, l, r = map(int, input().split())

min1 = n-l+1
max1 = 0
i = 2
for j in range(l-1):
    min1 += i
    i = i * 2

i = 1
for j in range(r-1):
    max1 += i
    i = i*2

max1 += (n-r+1)*i

print(min1,max1)