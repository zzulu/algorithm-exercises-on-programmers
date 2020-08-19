# def solution(seoul):
#     return '김서방은 {}에 있다'.format(seoul.index('Kim'))


def solution(seoul):
    for index, person in enumerate(seoul):
        if person == 'Kim': break
    return f'김서방은 {index}에 있다'


print(solution(['Jane', 'Kim'])) #=> '김서방은 1에 있다'
