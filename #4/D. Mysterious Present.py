n, w, h = map(int, input().split())

env = []

for i in range(n):
    env.append(list(map(int, input().split())))

env.sort(key=lambda a: a[1])
env.sort(key=lambda a: a[0])

for i in range(n):
    if not a:
        if i[0] >= w:
            a = True
            if i[1] >= h:
                break
    else:
        if i[1] >= h:
            break
