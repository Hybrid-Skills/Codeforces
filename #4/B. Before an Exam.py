d, sum_time = map(int, input().split())
min_time = []
max_time = []

for i in range(d):
    a = input().split()
    min_time.append(int(a[0]))
    max_time.append(int(a[1]))

if sum_time < sum(min_time) or sum_time > sum(max_time):
    print('NO')
else:
    print('YES')
    b = sum_time - sum(min_time)
    for i in range(d):
        print(min_time[i] + min((max_time[i] - min_time[i]), b), end=' ')

        b -= min((max_time[i] - min_time[i]), b)
