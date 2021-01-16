def solution(land):
    for y in range(len(land)-2, -1, -1):
        for x in range(4):
            land[y][x] += max(land[y+1][:x] + land[y+1][x+1:])
    return max(land[0])


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]])) #=> 16
