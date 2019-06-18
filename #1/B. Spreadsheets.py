# B. Spreadsheets

# In the popular spreadsheets systems (for example, in Excel) the
# following numeration of columns is used. The first column has
# number A, the second — number B, etc. till column 26 that is
# marked by Z. Then there are two-letter numbers: column 27 has
# number AA, 28 — AB, column 52 is marked by AZ. After ZZ there
# follow three-letter numbers, etc.

# The rows are marked by integer numbers starting with 1. The cell
# name is the concatenation of the column and the row numbers. For
# example, BC23 is the name for the cell that is in column 55, row 23.

# Sometimes another numeration system is used: RXCY, where X and Y
# are integer numbers, showing the column and the row numbers
# respectfully. For instance, R23C55 is the cell from the previous
# example.

# Your task is to write a program that reads the given sequence of
# cell coordinates and produce each item written according to the
# rules of another numeration system.


def convert_xy(ab):
    column = 0
    row = 0
    for i, char in enumerate(ab):
        if not char.isdigit():
            column = column * 26 + ord(char) - 96
        else:
            row = int(ab[i:])
            break
    print(f'R{row}C{column}')


def convert_ab(xy):
    i = xy.index('c')
    column = int(xy[i+1:])
    row = xy[1:i]
    answer = ''
    while column > 0:
        if column % 26 != 0:
            answer = chr(96 + (column % 26)) + answer
            column = column // 26
        else:
            answer = 'z' + answer
            column = column//26 - 1
    print(answer.upper() + row)


n = int(input())
for _ in range(n):
    question = input().lower()
    if question[0] != 'r':
        convert_xy(question)
    elif not question[1].isdigit():
        convert_xy(question)
    elif 'c' in question:
        convert_ab(question)
    else:
        convert_xy(question)