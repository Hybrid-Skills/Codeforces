# Question A. Winner

# The winner of the card game popular in Berland "Berlogging" is determined
# according to the following rules. If at the end of the game there is only one
# player with the maximum number of points, he is the winner. The situation
# becomes more difficult if the number of such players is more than one. During
# each round a player gains or loses a particular number of points. In the
# course of the game the number of points is registered in the line "name
# score", where name is a player's name, and score is the number of points
# gained in this round, which is an integer number. If score is negative, this
# means that the player has lost in the round. So, if two or more players have
# the maximum number of points (say, it equals to m) at the end of the game,
# than wins the one of them who scored at least m points first. Initially each
# player has 0 points. It's guaranteed that at the end of the game at least one
# player has a positive number of points.


n = int(input())
scores = []
num = []
maximum = 0

for _ in range(n):
    q = input().split()
    if q[0] in scores:
        scores[scores.index(q[0]) + 1] += int(q[1])
    else:
        scores = scores + [q[0], int(q[1])]
    if scores[scores.index(q[0]) + 1] > maximum:
        maximum = scores[scores.index(q[0]) + 1]
        winner = q[0]
for i in scores:
    if i is int:
        num.append(i)


print(winner)
