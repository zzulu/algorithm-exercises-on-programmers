def solution(progresses, speeds):
    result = []
    feature = 0
    while feature < len(progresses):
        for index in range(feature, len(progresses)):
            progresses[index] += speeds[index]

        deployed = 0
        for index in range(feature, len(progresses)):
            if progresses[index] < 100:
                break
            else:
                deployed += 1
                feature += 1
                
        if deployed:
            result.append(deployed)

    return result


print(solution([93,30,55], [1,30,5])) #=> [2,1]
