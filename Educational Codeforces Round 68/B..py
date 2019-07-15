q = int(input())


for _ in range(q):
    max1 = 0
    max2 = 0
    rows = []
    pos1 = []
    pos2 = []
    n, m = map(int, input().split())
    for i in range(n):
        row = input()
        count = row.count('*')
        rows.append(row)
        if max1 == count:
            pos1.append(i)
        elif max1 < count:
            pos1 = [i]
            max1 = count
    for i in range(m):
        count = 0
        for j in range(n):
            if rows[j][i] == '*':
                count += 1
        if max2 == count:
            pos2.append(i)
        elif max2 < count:
            pos2 = [i]
            max2 = count

    for i in pos1:
        for j in pos2:
            if rows[i][j] == '.':
                print((n - max1) + (m - max2) - 1)
                break
        else:
            continue
        break
    else:
        print((m - max1) + (n - max2))
