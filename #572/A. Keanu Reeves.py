n = int(input())
s = input()

if n % 2 != 0:
    print(1)
    print(''.join(s))
else:
    num0 = 0
    for i in s:
        if i == '0':
            num0 += 1
    if num0 != n / 2:
        print(1)
        print(''.join(s))
    else:
        print(2)
        print(s[0], end=' ')
        print(s[1:])
