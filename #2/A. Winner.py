n = int(input())
result = []
score_sum = {}
score_sum1 = {}

for _ in range(n):
    result.append(input().split())

for i in result:
    try:
        score_sum[i[0]] += int(i[1])
    except KeyError:
        score_sum[i[0]] = int(i[1])

winning_score = max(score_sum.values())

possible_winners = [key for (key, value) in score_sum.items() if value == winning_score]

if len(possible_winners) == 1:
    print(possible_winners[0])

else:
    for i in result:
        if i[0] in possible_winners:
            try:
                score_sum1[i[0]] += int(i[1])
            except KeyError:
                score_sum1[i[0]] = int(i[1])
            if score_sum1[i[0]] >= winning_score:
                print(i[0])
                break
