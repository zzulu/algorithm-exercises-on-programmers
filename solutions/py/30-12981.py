def solution(n, words):
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in words[:i]:
            return [(i%n)+1, (i//n)+1]
    else:
        return [0, 0]


print(solution(3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank'])) #=> [3, 3]
print(solution(5, ['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive'])) #=> [0, 0]
print(solution(2, ['hello', 'one', 'even', 'never', 'now', 'world', 'draw'])) #=> [1, 3]
