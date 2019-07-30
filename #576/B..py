h, l = map(int, input().split())
ans = round(((l**2 - h**2)/2)/h, 6)
print('{:.8f}'.format(((l**2 - h**2)/2)/h))