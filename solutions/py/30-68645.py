def solution(n):
    triangle = [[0]*(i+1) for i in range(n)]
    delta = [(1, 0), (0, 1), (-1, -1)] # y, x
    y, x, delta_index = 0, 0, 0

    for num in range(1, n*(n+1)//2+1):
        triangle[y][x] = num

        next_y, next_x = y + delta[delta_index%3][0], x + delta[delta_index%3][1]
        
        if not 0 <= next_y < n or not 0<= next_x < n or triangle[next_y][next_x]:
            delta_index += 1

        y, x = y + delta[delta_index%3][0], x + delta[delta_index%3][1]

    result = []
    for line in triangle:
        for number in line:
            result.append(number)
    return result


print(solution(4)) #=> [1, 2, 9, 3, 10, 8, 4, 5, 6, 7]
print(solution(5)) #=> [1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9]
print(solution(6)) #=> [1, 2, 15, 3, 16, 14, 4, 17, 21, 13, 5, 18, 19, 20, 12, 6, 7, 8, 9, 10, 11]
