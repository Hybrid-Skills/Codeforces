n = int(input())

for i in range(n//2):
    for i in range(n//2):
        print('W',end='')
        print('B',end='')
    if n%2 == 1:
        print('W')
    else:
        print('')
    for i in range(n//2):
        print('B',end='')
        print('W',end='')
    if n%2 == 1:
        print('B')
    else:
        print('')
if n%2 == 1:
    for i in range(n//2):
        print('W',end='')
        print('B',end='')
    print('W')