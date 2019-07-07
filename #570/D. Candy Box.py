q = int(input())

for _ in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    candy_num = [0] * (n+1)
    for i in a:
        candy_num[i] += 1

    candy_num.sort()
    candy_num.reverse()
    prev = 2 * 10**5 + 1
    gift = 0
    for i in candy_num:
        if i < prev:
            gift += i
            prev = i
        elif prev > 1:
            gift += prev - 1
            prev -= 1
        else:
            break
    print(gift)
