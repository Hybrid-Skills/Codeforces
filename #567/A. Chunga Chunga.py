xyz = input().split()
x = int(xyz[0])
y = int(xyz[1])
z = int(xyz[2])

max_coc = (x + y) // z
rem_x = x % z
rem_y = y % z

if rem_x + rem_y < z:
    print(str(max_coc) + " 0")
elif rem_x >= rem_y:
    print(str(max_coc) + " " + str(z - rem_x))
elif rem_y > rem_x:
    print(str(max_coc) + " " + str(z-rem_y))