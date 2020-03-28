def solution(s):
    p, y = 0, 0
    for c in s:
        if c == 'p' or c == 'P':
            p += 1
        elif c == 'y' or c == 'Y':
            y += 1

    return p == y
    # return s.lower().count('p') == s.lower().count('y')


print(solution('pPoooyY')) #=> True
print(solution('Pyy')) #=> False
