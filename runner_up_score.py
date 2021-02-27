# arr = [-7, -7, -7, -7, -6]
arr = [2, 3, 6, 6, 5]
# arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 6]

arr.sort()

arr_length = len(arr)
print(arr_length - 2)

runner_up = 0
for value in reversed(arr):
    if arr[arr_length] < value:
        print(arr_length)

