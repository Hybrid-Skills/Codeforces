n = int(input())
s = input()
m = int(input())

s_count = []

for i, char in enumerate(s):
    s_count.append(char)
    s_count.append(s_count.count(char))


for _ in range(m):
    t = input()
    t_count = []
    number_bought = 0
    if len(t) == 1:
        print(s.index(t) + 1)
    else:
        for i, char in enumerate(t):
            t_count.append(char)
            t_count.append(t_count.count(char))

        for i in range(0, len(t_count), 2):
            buying = t_count[i], t_count[i+1]
            for j in range(0, 2*n, 2):
                if s_count[j] == t_count[i] and s_count[j+1] == t_count[i+1]:
                    index = j
                    break
            number_bought = max(number_bought, index//2 + 1)

        print(number_bought)
