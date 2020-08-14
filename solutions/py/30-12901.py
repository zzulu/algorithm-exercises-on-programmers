def solution(a, b):
    week = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return week[(sum(month[:a])+b)%7]


print(solution(5, 24)) #=> 'TUE'
