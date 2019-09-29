n, k = map(int, input().split())

s = input()

if n == 1 and k >= 1:
    print('0')
    quit()
else:
    a = 0
    if k > a:
        if s[0] != '1':
            a += 1
            b = ['1']
        else:
            b = ['1']
    else:
        print(s)
        quit()

if k > a:
    for i in range(1, n):
        if s[i] != '0':
            b.append('0')
            a += 1
        else:
            b.append('0')
        if a == k:
            b.append(s[i+1:])
            break
else:
    b.append(s[1:])

print(''.join(b))