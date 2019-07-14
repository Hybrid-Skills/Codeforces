tiles = input().split()

s = []
m = []
p = []

for i in tiles:
    if i[1] == 's':
        s.append(int(i[0]))
    elif i[1] == 'p':
        p.append(int(i[0]))
    else:
        m.append(int(i[0]))

s.sort()
m.sort()
p.sort()


num_s = len(s)
num_p = len(p)
num_m = len(m)

if num_s == 3:
    if len(set(s)) == 1:
        print(0)
    elif len(set(s)) == 2:
        print(1)
    else:
        if s[0] == s[1] - 1:
            if s[1] == s[2] - 1:
                print(0)
            else:
                print(1)
        elif s[0] < s[1] - 2:
            if s[1] == s[2] - 1 or s[1] == s[2] - 2:
                print(1)
            else:
                print(2)
        else:
            print(1)
elif num_m == 3:
    if len(set(m)) == 1:
        print(0)
    elif len(set(m)) == 2:
        print(1)
    else:
        if m[0] == m[1] - 1:
            if m[1] == m[2] - 1:
                print(0)
            else:
                print(1)
        elif m[0] < m[1] - 2:
            if m[1] == m[2] - 1 or m[1] == m[2] - 2:
                print(1)
            else:
                print(2)
        else:
            print(1)
elif num_p == 3:
    if len(set(p)) == 1:
        print(0)
    elif len(set(p)) == 2:
        print(1)
    else:
        if p[0] == p[1] - 1:
            if p[1] == p[2] - 1:
                print(0)
            else:
                print(1)
        elif p[0] < p[1] - 2:
            if p[1] == p[2] - 1 or p[1] == p[2] - 2:
                print(1)
            else:
                print(2)
        else:
            print(1)
elif num_s == 2:
    if len(set(s)) == 1:
        print(1)
    else:
        if s[0] == s[1] - 1 or s[0] == s[1] - 2:
            print(1)
        else:
            print(2)
elif num_m == 2:
    if len(set(m)) == 1:
        print(1)
    else:
        if m[0] == m[1] - 1 or m[0] == m[1] - 2:
            print(1)
        else:
            print(2)
elif num_p == 2:
    if len(set(p)) == 1:
        print(1)
    else:
        if p[0] == p[1] - 1 or p[0] == p[1] - 2:
            print(1)
        else:
            print(2)
else:
    print(2)
