def solution(arr1, arr2):
    len_y, len_x = len(arr1), len(arr1[0])
    for y in range(len_y):
        for x in range(len_x):
            arr1[y][x] += arr2[y][x]
    return arr1


print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]])) #=>   [[4,6], [7,9]]
print(solution([[1], [2]], [[3], [4]])) #=> [[4], [6]]
