abcd = input().split()
abc = list(map(int,abcd[0:3]))
abc.sort()
a = abc[0]
b = abc[1]
c = abc[2]
d = int(abcd[3])


if (b - a) >= d and (c - b) >= d:
    print(0)
else:
    if (b-a) >= d > (c-b):
        print(d - (c-b))
    elif (c - b) >= d > (b - a):
        print(d - (b-a))
    else:
        print(d-(b-a) + d - (c-b))
