# Question #2
#
# You have a given picture with size w×h. Determine if the given picture has a single "+" shape or not.
# A "+" shape is described below:
#
# 1. A "+" shape has one center nonempty cell.
# 2. There should be some (at least one) consecutive non-empty cells in each direction from the center.
#    In other words, there should be a ray in each direction.
# 3. All other cells are empty.

# Find out if the given picture has single "+" shape.


def check_plus(q, total=0):

    # Finds the number of *s in the matrix
    for k in range(h):
        for l in range(w):
            if q[k][l] == '*':
                total += 1

    # Counter for number of pluses
    plus = 0
    for i in range(1, h-1):
        for j in range(1, w-1):
            if q[i][j] == '*':

                # finds if there is a plus and removes the plus stars from total *s
                if q[i-1][j] == q[i+1][j] == q[i][j-1] == q[i][j+1] == '*':

                    # deletes number of *s in the plus
                    total -= 1
                    plus += 1

                    # deletes * from upper branch of plus
                    for _ in range(1, i+1):
                        if q[i-_][j] == '*':
                            total -= 1
                        else:
                            break

                    # deletes * from left branch of plus
                    for __ in range(1, j+1):
                        if q[i][j - __] == '*':
                            total -= 1
                        else:
                            break

                    # deletes * from bottom branch of plus
                    for ___ in range(i+1, h):
                        if q[___][j] == '*':
                            total -= 1
                        else:
                            break

                    # deletes * from right branch of plus
                    for ____ in range(j+1, w):
                        if q[i][____] == '*':
                            total -= 1
                        else:
                            break

    # Checks if there are extra *s in the matrix and number of pluses
    if total == 0 and plus == 1:
        return 'YES'
    else:
        return 'NO'


hw = input().split()

h = int(hw[0])

w = int(hw[1])

question = []

for _________ in range(h):
    question.append(input())

print(check_plus(question))



