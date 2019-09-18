n = int(input())
x = list(map(int, input().split()))
even = 0

for i in x:
    if i % 2 == 0:
        even += 1

if even > n - even:
    print(n - even)
else:
    print(even)