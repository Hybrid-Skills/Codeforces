s = list(map(int,input().split()))

a = [[[1] for _ in range(10)] for _ in range(10)]

def call(i,j,c1,c2):
    if c1 > c2:
        x = c1 - c2 - 10
        y = c1 - c2
    else:
        x = c2 - c1
        y = c2 - c1 - 10

