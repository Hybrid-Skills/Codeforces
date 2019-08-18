s = input()
t = input()

for i in range(len(t)):
    j = 0
    while j < len(s):
        if t[i] == s[j]:
            j += 1
            break
        else:
            j += 1

ans_left = 