def solution(s):
    count, zero = 0, 0
    while s != '1':
        bi = ''
        for n in s:
            if n == '1':
                bi += n
            else:
                zero += 1
        q, s = len(bi), ''
        while q:
            q, r = q // 2, q % 2
            s += str(r)
        count += 1
    return [count, zero]


print(solution('110010101001')) #=> [3, 8]
print(solution('01110')) #=> [3, 3]
print(solution('1111111')) #=> [4, 1]
