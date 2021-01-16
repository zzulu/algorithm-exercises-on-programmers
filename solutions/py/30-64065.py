# def solution(s):
#     result = []
#     t = sorted(map(lambda n: list(map(int, n.split(','))), s[2:len(s)-2].split('},{')), key=lambda n: len(n))
#     for sub in t:
#         for n in sub:
#             if n not in result:
#                 result.append(n)
#                 break
#     return result


def solution(s):
    tu = map(lambda n: n.split(','), s[2:len(s)-2].split('},{'))
    d = {}
    for sub in tu:
        for n in sub:
            d[n] = d[n] + 1 if n in d else 1
    return [int(k) for k, v in sorted(d.items(), key=lambda i: i[1], reverse=True)]


print(solution('{{2},{2,1},{2,1,3},{2,1,3,4}}')) #=> [2, 1, 3, 4]
print(solution('{{1,2,3},{2,1},{1,2,4,3},{2}}')) #=> [2, 1, 3, 4]
print(solution('{{20,111},{111}}')) #=>  [111, 20]
print(solution('{{123}}')) #=>   [123]
print(solution('{{4,2,3},{3},{2,3,4,1},{2,3}}')) #=> [3, 2, 4, 1]
