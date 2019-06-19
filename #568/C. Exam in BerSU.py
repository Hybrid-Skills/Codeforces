nm = input().split()
n = int(nm[0])
m = int(nm[1])

t = input().split()
answer = []
sum_prev = 0

for i in range(n):
    sum_prev += int(t[i])
    number_removed = 0
    if sum_prev <= m:
        answer.append('0')
    else:
        t1 = list(map(int, t))
        sum_prev1 = sum_prev
        while sum_prev1 > m:
            j = i - number_removed
            sum_prev1 -= max(t1[0:j])
            t1.remove(max(t1[0:j]))
            number_removed += 1
        answer.append(str(number_removed))

print(' '.join(answer))
