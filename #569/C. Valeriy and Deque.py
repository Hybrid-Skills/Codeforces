nq = input().split()
n = int(nq[0])
q = int(nq[1])
arr = list(map(int, input().split()))
arr_q = []
for _ in range(q):
    arr_q.append(int(input()))


largest1 = max(arr)
new_arr = []
for i in arr:
    new_arr.append(i)
for i in range(n-1):
    if new_arr[i] > new_arr[i+1]:
        new_arr[i:i+2] = [new_arr[i+1], new_arr[i]]


for m in arr_q:
    if m < n:
        largest = max(arr[:m])
        print(f'{largest} {arr[m]}')

    else:
        m = ((m-n) % (n-1)) + n
        print(f'{largest1} {new_arr[m - n]}')
