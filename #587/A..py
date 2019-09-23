def arr():
    return list(map(int, input().split()))

n = int(input())
s = input()

i = 0
step = 0
l = []

while i<len(s):
    l.append(s[i])
    if s[i] == 'a':
        if s[i+1] == 'b':
            pass
        else:
            step += 1
        l.append('b')
    elif s[i] == 'b':
        if s[i+1] == 'a':
            pass
        else:
            step += 1
        l.append('a')
    i += 2

print(step)
print(''.join(l))