import math

n, m, k = [int(i) for i in input().split()]

p = [int(i) for i in input().split()]
num_del = 0
moves = 0
len_p = m

while len_p > 0:
    last = k * math.ceil((p[0] - num_del) / k) + num_del

    for i in range(len_p):
        if p[i] > last:
            p = p[i:]
            len_p -= i
            num_del += i
            moves += 1
            break
        elif i == len_p - 1:
            num_del += len_p
            p = []
            len_p = 0
            moves += 1

print(moves)
