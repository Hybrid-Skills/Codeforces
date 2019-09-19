n = int(input())
ant = []

for i in range(n):
    ant.append([int(i) for i in input().split()])

for _ in range(int(input())):
    location = [int(i) for i in input().split()]
