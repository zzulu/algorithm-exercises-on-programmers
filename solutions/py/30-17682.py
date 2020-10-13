def solution(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}    
    stack, scores = [], []
    for char in dartResult:
        if char.isnumeric():
            stack.append(char)
        elif char == '*':
            scores, recent_of_scores = scores[:-2], scores[-2:]
            scores += [s*2 for s in recent_of_scores]
        elif char == '#':
            scores[-1] *= -1
        else:
            scores.append(int(''.join([s for s in stack]))**bonus[char])
            stack = []
    return sum(scores)


print(solution('1S2D*3T')) #=> 37
print(solution('1D2S#10S')) #=> 9
print(solution('1D2S0T')) #=> 3
print(solution('1S*2T*3S')) #=> 23
print(solution('1D#2S*3S')) #=> 5
print(solution('1T2D3D#')) #=> -4
print(solution('1D2S3T*')) #=> 59
