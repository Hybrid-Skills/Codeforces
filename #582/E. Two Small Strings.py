n = int(input())

s = input()
t = input()
characters = ['a', 'b', 'c']

print('YES')

if s[0] == s[1] and t[0] == t[1]:
    x = 'abc'
    print(x*n)

elif s[0] == s[1]:
    if 'a' not in t:
        x = t[0] + 'a' + t[1]
    elif 'b' not in t:
        x = t[0] + 'b' + t[1]
    else:
        x = t[0] + 'c' + t[1]
    print(x*n)

elif t[0] == t[1]:
    if 'a' not in s:
        x = s[0] + 'a' + s[1]
    elif 'b' not in s:
        x = s[0] + 'b' + s[1]
    else:
        x = s[0] + 'c' + s[1]
    print(x*n)

elif (s[1] == t[1]) or (s[0] == t[0]):
    if s[1] == t[1]:
        characters.remove(s[1])
        print(s[1]*n + ''.join(characters)*n)
    else:
        characters.remove(s[0])
        print(''.join(characters)*n + s[0]*n)

elif s[0] == t[1] and s[1] == t[0]:
    characters.remove(s[0])
    characters.remove(s[1])
    print(s[0]*n + characters[0]*n + s[1]*n)

else:
    if 'a' not in s:
        x = s[0] + 'a' + s[1]
    elif 'b' not in s:
        x = s[0] + 'b' + s[1]
    else:
        x = s[0] + 'c' + s[1]
    print(x*n)
