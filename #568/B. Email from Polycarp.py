def check_possible(original, typed):
    j = 0
    for char in typed:
        try:
            if char == original[j]:
                j += 1
        except IndexError:
            pass
        if char == original[abs(j-1)]:
            pass
        else:
            return 'NO'
    else:
        if j == len(original):
            return 'YES'
        else:
            return 'NO'


n = int(input())
for _ in range(n):
    original1 = input()
    typed1 = input()
    print(check_possible(original1, typed1))
