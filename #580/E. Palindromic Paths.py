import sys

n = int(input())

arr = [[0 for i in range(n)] for j in range(n)]

arr[0][0] = 1

for i in range(0, n, 2):
    if i != n-1:
        sys.stdout.flush('?', 1, i+1, 1, i+3)
        x = int(input())
        if x == 1:
            arr[0][i+2] = arr[0][i]
        else:
            if arr[0][i] == 0:
                arr[0][i+2] = 1
            else:
                arr[0][i+2] = 0

    for j in range(0, n-2, 2):
        if i != n-1 or j != n-3:
            sys.stdout.flush('?', j+1, i+1, j+3, i+1)
            x = int(input())
            if x == 1:
                arr[j+2][i] = arr[j][i]
            else:
                if arr[j][i] == 0:
                    arr[j+2][i] = 1
                else:
                    arr[j+2][i] = 0

sys.stdout.flush('?', 1, 1, 2, 2)
x = int(input())
if x == 1:
    arr[1][1] = 1
else:
    arr[1][1] = 0

for i in range(1,n-1,2):
    if i != n-2:
        sys.stdout.flush('?', 1, i+1, 1, i+3)
        x = int(input())
        if x == 1:
            arr[0][i + 2] = arr[0][i]
        else:
            if arr[0][i] == 0:
                arr[0][i + 2] = 1
            else:
                arr[0][i + 2] = 0

    for j in range(1, n-3, 2):
        sys.stdout.flush('?', j + 1, i + 1, j + 3, i + 1)
        x = int(input())
        if x == 1:
            arr[j + 2][i] = arr[j][i]
        else:
            if arr[j][i] == 0:
                arr[j + 2][i] = 1
            else:
                arr[j + 2][i] = 0


print('!')
for i in range(n):
    print(''.join(list(map(str, arr[i]))))