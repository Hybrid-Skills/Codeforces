n = int(input())
d = {}

for i in range(n):
    a = input()

    try:
        print(a + str(d[a]))
        d[a] += 1
    except KeyError:
        print('OK')
        d[a] = 1