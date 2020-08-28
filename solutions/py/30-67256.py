def distance(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


def solution(numbers, hand):
    # keypad = [[1, 4, 7, '*'],
    #           [2, 5, 8, 0],
    #           [3, 6, 9, '#']]

    left = (0, 3)
    right = (2, 3)

    result = ''
    for number in numbers:
        if number == 0:
            q, r = 3, 2
        else:
            q, r = number // 3, number % 3

        if r == 2:
            ld, rd = distance(left, (1, q)), distance(right, (1, q))
            if ld < rd:
                left = (1, q)
                result += 'L'
            elif ld > rd:
                right = (1, q)
                result += 'R'
            else:
                if hand == 'left':
                    left = (1, q)
                    result += 'L'
                else:
                    right = (1, q)
                    result += 'R'
        elif r == 1:
            left = (0, q)
            result += 'L'
        elif r == 0:
            right = (2, q-1)
            result += 'R'

    return result


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right')) #=> 'LRLLLRLLRRL'
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left')) #=> 'LRLLRRLLLRR'
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right')) #=> 'LLRLLRLLRL'
