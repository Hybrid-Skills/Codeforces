l, r = map(int, input().split())

for i in range(l,r+1):
    if len(str(i)) == len(set(str(i))):
        print(i)
        break
else:
    print(-1)