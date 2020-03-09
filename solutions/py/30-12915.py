def solution(strings, n):
    start_i = 0
    for start_i in range(len(strings)):
        index = start_i
        for i in range(start_i, len(strings)):
            if strings[index][n] > strings[i][n]:
                index = i
            elif strings[index][n] == strings[i][n] and strings[index] > strings[i]:
                index = i
        strings[start_i], strings[index] = strings[index], strings[start_i]
    return strings


print(solution(['sun', 'bed', 'car'], 1)) # ['car', 'bed', 'sun']
print(solution(['abce', 'abcd', 'cdx'], 2)) # ['abcd', 'abce', 'cdx']
