l = int(input())
n = int(input())
x = 0
y = 0

if l % 2 == 0:
    str_x = str(n)[0:l//2]
    str_y = str(n)[l//2:l]
    str_x_right = str_x
    str_x_left = str_x
    str_y_left = str_y
    str_y_right = str_y

else:
    str_x_left = str(n)[0:l // 2]
    str_y_left = str(n)[l // 2:l]
    str_x_right = str(n)[0:(l//2) + 1]
    str_y_right = str(n)[(l//2)+1:l]

i=1
j=0

while str_y_right[j] == "0" and str_x_left[-i] == "0":
    j += 1
    i += 1

str_x_right += "0"*j
str_y_right = str_y_right[j:]
str_y_left = str_x_left[-i:] + str_y_left
str_x_left = str_x_left[:-i]

sum_moving_right = int(str_x_right) + int(str_y_right)

try:
    sum_moving_left = int(str_x_left) + int(str_y_left)
except ValueError:
    sum_moving_left = int(str_y_left)

if str_y_right[0] == '0':
    print(sum_moving_left)
elif str_y_left[0] == '0':
    print(sum_moving_right)
else:
    print(min(sum_moving_right, sum_moving_left))

