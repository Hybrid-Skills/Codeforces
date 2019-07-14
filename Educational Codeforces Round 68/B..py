q = int(input())
minimum = minimum_column = 46 * 10 ** 6

for _ in range(q):
    n, m = [int(i) for i in input().split()]
    rows = []
    for __ in range(n):
        rows.append(input())
        total = 0
        for i in rows[-1]:
            total += ord(i)
        minimum = min(total, minimum)

    minutes_rows = (minimum - (m * 42)) //4

    print(minutes_rows)
    # columns = []
    # for i in range(m):
    #     columns.append([])
    # for i in range(m):
    #     for j in range(n):
    #         columns[i].append(rows[j][i])
    #     total_column = 0
    #     for j in columns[i]:
    #         total_column += ord(j)
    #     minimum_column = min(total_column, minimum_column)
    #
    # minutes = minutes_rows + (minimum_column - (n-42)) / 4
    # print(minutes)