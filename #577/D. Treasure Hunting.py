n, m, k, q = map(int, input().split())

t = []

for _ in range(k):
    t.append(list(map(int, input().split())))

q = list(map(int, input().split()))

pos = [1, 1]

t.sort(key=lambda a: a[0])


def steps(pos,q):
    left_steps = 0
    right_steps = 0



steps = 0
steps += steps(pos, q)