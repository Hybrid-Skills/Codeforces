n = int(input())

x_appears1 = []
x_appears2 = []
x_appears3 = []
x_side = []
y_appears1 = []
y_appears2 = []
y_appears3 = []
y_side = []
points = []


for _ in range(4 * n + 1):
    x, y = map(int, input().split())
    points.append([x, y])
    if x in x_appears1:
        x_appears2.append(x)
        x_appears1.remove(x)
    elif x in x_appears2:
        x_appears3.append(x)
        x_appears2.remove(x)
    elif x in x_appears3:
        x_side.append(x)
        x_appears3.remove(x)
    elif x in x_side:
        pass
    else:
        y_appears1.append(y)
    if y in y_appears1:
        y_appears2.append(y)
        y_appears1.remove(y)
    elif y in y_appears2:
        y_appears3.append(y)
        y_appears2.remove(y)
    elif y in y_appears3:
        y_side.append(y)
        y_appears3.remove(y)
    elif y in y_side:
        pass
    else:
        y_appears1.append(y)

