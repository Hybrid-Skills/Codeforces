n = int(input())
a = input()

for i in a:
    if i == 'n':
        print(1, end=' ')
        n-=3

for i in range(n//4):
    print(0, end=' ')