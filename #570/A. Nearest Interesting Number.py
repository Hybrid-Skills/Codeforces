n = input()

sum1 = 0
for i in n:
    sum1 += int(i)

if sum1 % 4 == 0:
    print(n)

else:
    while sum1 % 4 != 0:
        n = str(1+int(n))
        sum1 = 0
        for i in n:
            sum1 += int(i)
    print(n)