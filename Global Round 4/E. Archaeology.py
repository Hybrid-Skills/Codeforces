s = input()
n = len(s)
# x = 0
# y = n-1
# ans = ''
# flag = False
#
# while x < y - 2:
#     if s[x] == s[y] or s[x] == s[y-1]:
#         ans += s[x]
#     else:
#         ans += s[x+1]
#     x += 2
#     y -= 2
#
# if y - x >= 1:
#     print(ans + s[x] + ans[::-1])
# else:
#     print(ans + ans[::-1])

i, j = 0, n - 1
ans = []
t = n // 4
for i in range(t):
    x = i*2
    y = n - 2 - i * 2
    if s[x] == s[y] or s[x] == s[y+1]:
        ans.append(s[x])
    else:
        ans.append(s[x+1])
if n % 4 >= 2:
    ans = ans + [s[n // 2]] + ans[::-1]
else:
    ans = ans+ans[::-1]
print(''.join(ans))