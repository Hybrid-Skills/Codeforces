n = int(input())
a = [int(i) for i in input().split()]

total = sum(a)
final = n * (n-1) // 2
repeated = []
count = {}

for i in a:
    try:
        count[i] += 1
        repeated.append(i)
    except KeyError:
        count[i] = 1
    if len(repeated) >= 2:
        break


moves = total - final

if len(repeated) > 1:
    print('cslnb')

elif 0 in repeated:
    print('cslnb')

elif len(repeated) == 1 and repeated[0] - 1 in a:
    print('cslnb')

else:
    if moves % 2 == 0 or moves <= 0:
        print('cslnb')
    else:
        print('sjfnb')
