def solution(answers):
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    correct = {1: 0, 2: 0, 3: 0}
    for (index, answer) in enumerate(answers):
        if student1[index%5] == answer:
            correct[1] += 1
            
        if student2[index%8] == answer:
            correct[2] += 1
            
        if student3[index%10] == answer:
            correct[3] += 1
    
    highest = []
    for student, score in correct.items():
        if not highest or score == correct[highest[0]]:
            highest.append(student)
        elif score > correct[highest[0]]:
            highest.clear()
            highest.append(student)
    
    return highest


print(solution([1,2,3,4,5])) # [1]
print(solution([1,3,2,4,2])) # [1,2,3]
