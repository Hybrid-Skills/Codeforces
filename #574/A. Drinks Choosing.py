n, k = map(int, input().split())

drink = {}
happy = 0

for _ in range(n):
    i = int(input())
    try:
        drink[i] += 1

    except KeyError:
        drink[i] = 1

for i in drink.values():
    happy += i//2

if n % 2 == 0:
    print(happy * 2 + n//2 - happy)
else:
    print(happy*2 + n//2 - happy + 1)
