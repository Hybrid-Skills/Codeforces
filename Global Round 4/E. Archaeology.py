s = input()

i = 0
j = -1
part1 = ''
part2 = ''


while i < len(s) and j >= -len(s):
    if s[i] == s[j]:
        part1 += s[i]
        part2 = s[i] + part2
    else:
        for x in range(len(s)):
