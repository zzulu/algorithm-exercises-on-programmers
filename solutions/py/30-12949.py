def solution(arr1, arr2):
    m, k, n = len(arr1), len(arr1[0]), len(arr2[0])
    result = [[ 0 for _ in range(n)] for _ in range(m)]

    for y in range(m):
        for x in range(n):
            for c in range(k):
                result[y][x] += arr1[y][c] * arr2[c][x]

    return result


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])) #=> [[15, 15], [15, 15], [15, 15]]
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]])) #=> [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
