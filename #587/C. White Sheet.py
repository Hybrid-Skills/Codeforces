x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())


def check_rect1(x,y):
    if x3 <= x <= x4 and y3 <= y <= y4:
        return True
    else:
        return False


def check_rect2(x,y):
    if x5 <= x <= x6 and y5 <= y <= y6:
        return True
    else:
        return False


if not (check_rect1(x1,y1) or check_rect2(x1,y1)):
    print('YES')

elif not (check_rect1(x2,y1) or check_rect2(x2,y1)):
    print('YES')

elif not (check_rect1(x2,y2) or check_rect2(x2,y2)):
    print('YES')

elif not (check_rect1(x1,y2) or check_rect2(x1,y2)):
    print('YES')

else:
    if check_rect2(x1,y1) and check_rect2(x2,y1) and check_rect1(x1,y2) and check_rect1(x2,y2):
        if y6 < y3 :
            print('YES')
        else:
            print('NO')
    elif check_rect1(x1, y1) and check_rect1(x2, y1) and check_rect2(x1, y2) and check_rect2(x2, y2):
        if y4 < y5:
            print('YES')
        else:
            print('NO')
    elif check_rect1(x1, y1) and check_rect2(x2, y1) and check_rect1(x1, y2) and check_rect2(x2, y2):
        if x4 < x5:
            print('YES')
        else:
            print('NO')
    elif check_rect2(x1, y1) and check_rect1(x2, y1) and check_rect2(x1, y2) and check_rect1(x2, y2):
        if x6 < x3:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')