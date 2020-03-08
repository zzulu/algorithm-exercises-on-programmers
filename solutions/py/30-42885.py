def solution(people, limit):
    people.sort()
    boats = 0
    left_index, right_index = 0, len(people)
    while left_index < right_index and right_index > 0:
        right_index -= 1
        if limit - people[right_index] >= 40 or people[right_index] <= 200:
            if people[left_index] + people[right_index] <= limit:
                left_index += 1
        boats += 1
    return boats

print(solution([70, 50, 80, 50], 100)) #=> 3
print(solution([70, 80, 50], 100)) #=> 3
