from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
dic = defaultdict(int)

d = 1
e = [0]

for i in range(n):
    if a[i] < 0:
        if dic[-1*a[i]] == 0:
            print(-1)
            quit()
        elif dic[-1*a[i]] == 1:
            dic[-1*a[i]] += 1
            e[-1] += 1
        else:
            print(-1)
            quit()

    else:
        if dic[a[i]] == 0:
            e[-1] += 1
            dic[a[i]] += 1
        elif dic[a[i]] == 2:
            x = dic.values()
            for j in x:
                if j != 2 and j != 0:
                    print(-1)
                    quit()
            else:
                d += 1
                e.append(1)
                dic = defaultdict(int)
                dic[a[i]] = 1
        else:
            print(-1)
            quit()

a = dic.values()

for i in a:
    if i != 2 and i != 0:
        print(-1)
        quit()

print(d)
print(' '.join(map(str,e)))
