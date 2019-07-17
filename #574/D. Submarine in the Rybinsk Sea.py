n = int(input())

question = input().split()

number = 0
carry = 0

for i in range(n):
    question[i] = list(map(int,list(question[i])))

transposed = list(zip(*question))

for i in range(1, len(question[0])+1):
    query = n*sum(transposed[-i]) + carry
    number += (10**(2*i-2))*(query % 10)
    carry = query//10
    query = n * sum(transposed[-i]) + carry
    number += (10 ** (2*i-1)) * (query % 10)
    carry = query // 10

number += 10**(2*len(question[0])) * carry

print(number % 998244353)