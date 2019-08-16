n = int(input())

s = input()

q = [0 for i in range(10)]

for i in s:
    if i.isdigit():
        q[int(i)] = 0
    elif i == 'L':
        for j in range(10):
            if q[j] == 0:
                q[j] = 1
                break
    else:
        for j in range(10):
            if q[10-j-1] == 0:
                q[10-j-1] = 1
                break

print(''.join(map(str,q)))