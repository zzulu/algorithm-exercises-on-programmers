def solution(arr):
    answer = []
    for n in arr:
        if not answer or answer[-1] != n:
            answer.append(n)
    return answer


print(solution([1,1,3,3,0,1,1])) #=> [1, 3, 0, 1]
print(solution([4,4,4,3,3])) #=> [4, 3]
