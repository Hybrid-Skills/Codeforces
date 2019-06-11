def check_plus(q, total=0):
    for k in range(h):
        for l in range(w):
            if q[k][l] == '*':
                total += 1
    plus = 0

    for i in range(1, h-1):
        for j in range(1, w-1):
            if q[i][j] == '*':
                if q[i-1][j] == q[i+1][j] == q[i][j-1] == q[i][j+1] == '*':
                    total -= 1
                    plus += 1
                    for _ in range(1, i+1):
                        if q[i-_][j] == '*':
                            total -= 1
                        else:
                            break
                    for __ in range(1, j+1):
                        if q[i][j - __] == '*':
                            total -= 1
                        else:
                            break
                    for ___ in range(i+1, h):
                        if q[___][j] == '*':
                            total -= 1
                        else:
                            break
                    for ____ in range(j+1, w):
                        if q[i][____] == '*':
                            total -= 1
                        else:
                            break
    print(total)
    if total == 0 and plus == 1:
        return 'YES'
    else:
        return 'NO'


hw = input().split()

h = int(hw[0])

w = int(hw[1])

question = []

for _________ in range(h):
    question.append(input())

print(check_plus(question))



