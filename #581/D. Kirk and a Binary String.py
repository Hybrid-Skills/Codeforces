n = input()

s = ''

for i in range(len(n)):

    if n[i] == '1':
        if i != len(n) - 1:
            if n[i+1] == '0':
                s += '1'
            else:
                s += '0'
        else:
            s += '0'
    else:
        s += '0'
    # print(s)

print(s)