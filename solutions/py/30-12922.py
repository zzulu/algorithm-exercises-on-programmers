def solution(n):
    chars = ['수', '박']
    word = ''
    for i in range(n):
        word += chars[i%2]
    return word


print(solution(3)) #=> '수박수'
print(solution(4)) #=> '수박수박'
