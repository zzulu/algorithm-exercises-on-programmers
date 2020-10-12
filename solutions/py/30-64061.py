def solution(board, moves):
    basket, crushed = [], 0
    for move in moves:
        for y in range(len(board)):
            if board[y][move-1]:
                stuff = board[y][move-1]
                board[y][move-1] = 0
                if basket and basket[-1] == stuff:
                    basket.pop()
                    crushed += 2
                else:
                    basket.append(stuff)
                break
    return crushed


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])) #=> 4
