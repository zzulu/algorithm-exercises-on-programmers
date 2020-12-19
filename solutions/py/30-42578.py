def solution(clothes):
    closet = {}
    for cloth in clothes:
        name, category = cloth
        if category in closet.keys():
            closet[category] += 1
        else:
            closet[category] = 1

    result = 1
    for value in closet.values():
        result *= value+1

    return result - 1


print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']])) #=> 5
print(solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']])) #=> 3
