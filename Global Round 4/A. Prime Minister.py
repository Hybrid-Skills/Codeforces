n = int(input())

a = [int(i) for i in input().split()]

total_seats = sum(a)
sum_seats = a[0]
party = ['1']
i = 0


def check_double(i):
    if a[0] >= 2*a[i]:
        return True
    else:
        return False


while sum_seats <= total_seats/2 and i <= n-2:
    i += 1
    if check_double(i):
        sum_seats += a[i]
        party.append(str(i+1))

if sum_seats > total_seats / 2:
    print(len(party))
    print(' '.join(party))

else:
    print(0)