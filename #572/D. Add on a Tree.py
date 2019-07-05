n = int(input())
master = []
appears1 = []
appears2 = []

for _ in range(n-1):
    uv = input().split()
    if uv[0] in appears1:
        appears1.remove(uv[0])
        appears2.append(uv[0])
    elif uv[0] in appears2:
        appears2.remove(uv[0])
    else:
        appears1.append(uv[0])
    if uv[1] in appears1:
        appears1.remove(uv[1])
        appears2.append(uv[1])
    elif uv[1] in appears2:
        appears2.remove(uv[1])
    else:
        appears1.append(uv[1])

if len(appears2)>0:
    print('NO')
else:
    print('YES')