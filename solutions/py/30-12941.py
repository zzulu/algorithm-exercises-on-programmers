def solution(A,B):
    A.sort(); B.sort(reverse=True)

    result = 0
    for i in range(len(A)):
        result += A[i]*B[i]

    return result


print(solution([1, 4, 2], [5, 4, 4])) #=> 29
print(solution([1, 2], [3, 4])) #=> 10
