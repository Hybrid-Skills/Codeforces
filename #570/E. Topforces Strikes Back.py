q = int(input())
for _ in range(q):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    a.reverse()
    answer = 0
    for i, val in enumerate(a):
        if val > answer / 3:
            answer1 = val
            no_used = 1
            for j in range(i+1, n):
                if val % a[j] != 0 and no_used < 3:
                    answer1 += a[j]
                    no_used += 1
                elif no_used == 3:
                    break
            if answer1 > answer:
                answer = answer1
        else:
            break
    print(answer)
