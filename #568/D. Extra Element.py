def extra_element(b, b1):
    record = []
    if len(b) <= 3:
        return 1
    b1.sort()
    c1 = b1[1] - b1[0]
    c2 = b1[2] - b1[1]
    c3 = b1[3] - b1[2]

    a = b1[0]
    j = 0

    if c1 == c2:
        c = c1
    elif c1 == c3 + c2:
        c = c1
    elif c2 == c3:
        c = c2
        a = b1[1]
        j = 1
    elif c1 + c2 == c3:
        c = c3
    else:
        return -1

    for value in b1:
        if value == a + j * c:
            pass
        else:
            record.append(b.index(value))
            b1.remove(value)
        j += 1
    if len(record) == 1:
        return record[0] + 1
    elif len(record) == 0:
        return 1
    else:
        return -1


n = int(input())
b1 = b = list(map(int, input().split()))
print(extra_element(b, b1))
