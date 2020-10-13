def comp(arr, l):
    value = arr[0][0]
    all_same = True
    for y in range(l):
        for x in range(l):
            if arr[y][x] != value:
                all_same = False
        if not all_same:
            break
    
    if all_same:
        return f'{value}'
    else:
        up = arr[0:l//2]
        up_left = [ row[0:l//2] for row in up]
        up_right = [ row[l//2:] for row in up]
        down = arr[l//2:]
        down_left = [ row[0:l//2] for row in down]
        down_right = [ row[l//2:] for row in down]
        return comp(up_left, l//2) + comp(up_right, l//2) + comp(down_left, l//2) + comp(down_right, l//2)
    
def solution(arr):
    result = comp(arr, len(arr))
    return [result.count('0'), result.count('1')]


print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])) #=> [4, 9]
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])) #=> [10, 15]
