n = int(input())

question = input().split()

number = 0

for i in range(n):
    question[i] = list(map(int, list(question[i])))

j = 0
transposed = [[], [], [], [], [], [], [], [], [], []]
while j <= 9:
    for i in range(n):
        try:
            transposed[j].append(question[i][-j-1])
        except IndexError:
            pass
    j += 1


max_digits = 0
for i in range(10):
    if not transposed[i]:
        max_digits = i
        break
else:
    max_digits = 10

for i in range(max_digits):
    temp_sum = sum(transposed[i])

    number += (10 ** (2*i)) * 11 * len(transposed[i]) * temp_sum

    if i > 0:
        j = 1
        while j <= 9:
            if i >= j:
                number += ((10**(2*i + 1 - j)) * (2 * (len(transposed[i-j]) - len(transposed[i-j+1])))*temp_sum)
            j += 1

print(number % 998244353)
