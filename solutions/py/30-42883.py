def solution(number, k):
    answer = ''
    for n in number:
        while answer and k > 0 and int(answer[-1]) < int(n):
            answer = answer[:len(answer)-1]
            k -= 1
        answer += n
    if k > 0:
        answer = answer[:len(answer)-k]
    return answer


print(solution('1924', 2)) #=> '94'
print(solution('1231234', 3)) #=> '3234'
print(solution('4177252841', 4)) #=> '775841'
print(solution('4321', 3)) #=> '4'
