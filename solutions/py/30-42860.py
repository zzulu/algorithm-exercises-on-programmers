def solution(name):
    count = 0
    need_to_change = []

    for index, char in enumerate(name):
        if not char == 'A' and index != 0:
            need_to_change.append(index)
        count += ord(char)-ord('A') if ord(char)-ord('A') < ord('Z')+1-ord(char) else ord('Z')+1-ord(char)

    index = 0
    while need_to_change:
        if index < need_to_change[0]:
            r = need_to_change[0] - index
            l = len(name) - (need_to_change[-1] - index)
        else:
            r = len(name) - (index - need_to_change[0])
            l = index - need_to_change[-1]

        if r <= l:
            count += r
            index = need_to_change[0]
            need_to_change.pop(0)
        else:
            count += l
            index = need_to_change[-1]
            need_to_change.pop()

    return count


print(solution('JEROEN')) #=> 56
print(solution('JAN')) #=> 23
print(solution('AAA')) #=> 0
print(solution('BBB')) #=> 5
print(solution('AABA')) #=> 3
print(solution('CACAAAAB')) #=> 9
