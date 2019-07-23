n = int(input())

a = [int(i) for i in input().split()]

highest = a.index(n)

number = 0
flag = False

for i in range(n):
    if i <= highest:
        if number >= a[i]:
            print('NO')
            break
        else:
            number = a[i]
    else:
        if number <= a[i]:
            print('NO')
            break
        else:
            number = a[i]

else:
    print('YES')