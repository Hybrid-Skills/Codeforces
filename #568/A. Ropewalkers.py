abcd = input().split()
abc = abcd[0:3]
abc.sort()
a = int(abc[0])
b = int(abc[1])
c = int(abc[2])
d = int(abcd[3])

if abs(a-b) >= d and abs(b-c) >= d:
    print(0)
else:
    if abs(a-b) >= d and not abs(b-c) >= d:
        print(d-abs(b-c))
    elif abs(b-c) >= d and not abs(a-b) >= d:
        print(d - abs(a-b))
    else:
        print(d-abs(a-b) + d - abs(b-c))
