def solution(brown, yellow):
    square = brown + yellow
    carpets = [[square // h, h] for h in range(2, square//2+1) if square % h == 0 and square // h >= h]

    for carpet in carpets:
        if brown == (carpet[0]*2 + carpet[1]*2 - 4):
            return carpet


print(solution(10, 2)) #=> [4, 3]
print(solution(8, 1)) #=> [3, 3]
print(solution(24, 24)) #=> [8, 6]
