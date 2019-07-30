s = input()
t = input()

diff_vertical = int(s[1]) - int(t[1])
diff_hor = ord(s[0]) - ord(t[0])

print(max(abs(diff_hor), abs(diff_vertical)))


while True:
    if diff_vertical > 0:
        if diff_hor > 0:
            print('LD')
            diff_hor -= 1
            diff_vertical -= 1
        elif diff_hor < 0:
            print('RD')
            diff_hor += 1
            diff_vertical -= 1
        else:
            print('D')
            diff_vertical -= 1
    elif diff_vertical < 0:
        if diff_hor > 0:
            print('LU')
            diff_hor -= 1
            diff_vertical += 1
        elif diff_hor < 0:
            print('RU')
            diff_hor += 1
            diff_vertical += 1
        else:
            print('U')
            diff_vertical += 1
    else:
        if diff_hor > 0:
            print('L')
            diff_hor -= 1
        elif diff_hor < 0:
            print('R')
            diff_hor += 1
        else:
            break