hw = [int(i) for i in input().split()]
h = hw[0]
w = hw[1]
r = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
total = 0
ans = 1

for i in range(w):
    for j in range(c[i]):
        if r[j] == i:
            print(0)
            quit()

for i in range(h):
    for j in range(r[i]):
        if c[j] == i:
            print(0)
            flag = True
            quit()

for i in range(h):
    for j in range(w):
        if j > r[i] and i > c[j]:
            total += 1

for i in range(total):
    ans = (ans*2)%1000000007

print(ans)