from collections import defaultdict

s = [i for i in input()]
d = defaultdict(str)

for _ in range(int(input())):
    a, b, c = input().split()

    if a == '1':
        s[int(b) - 1] = c

    else:
        print(len(set(s[int(b)-1:int(c)])))
    # print(s)
