flag = []

nm = input().split()
n = int(nm[0])
m = int(nm[1])

for _ in range(n):
    flag.append(input())


def check_flag(i, j, l, h):
    for _ in range(h):
        if len(set(flag[i+_][j:j+l])) != 1:
            return False
    if set(flag[i + h/3][j:j+l]) == set(flag[i][j:j+l]) or set(flag[i + h/3][j:j+l]) == set(flag[i + 2 * h/3][j:j+l]):
        return False
    else:
        return True


number_flags = 0

for h in range(1, n // 3):
    for i in range(n):
        c = 0
        while c <= m:
            for length in range(1, m-i):
                if check_flag(i, c, length, h):
                    number_flags += length
                else:
                    break
                    c += length

print(number_flags)
