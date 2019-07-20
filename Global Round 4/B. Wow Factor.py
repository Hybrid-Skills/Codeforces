s = input()
n = len(s)
t = []
wow = 0
w = 0

for i in range(n-1):
    if s[i] == 'v' and s[i+1] == 'v':
        w += 1
    elif s[i] == 'o':
        t.append(w)

for i in t:
    wow += i * (w - i)

print(wow)
