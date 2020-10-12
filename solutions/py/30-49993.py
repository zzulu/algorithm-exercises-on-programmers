def solution(skill, skill_trees):
    length = len(skill)
    able_trees = 0
    for skill_tree in skill_trees:
        index = 0
        for s in skill_tree:
            if index < length:
                if s == skill[index]:
                    index += 1
                elif s in skill[index+1:]:
                    break
        else:
            able_trees += 1
    return able_trees


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])) #=> 2
