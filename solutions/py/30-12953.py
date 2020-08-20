def gcd(a, b):
    x = a if a < b else b
    for n in range(x, 0, -1):
        if a % n == 0 and b % n == 0:
            break
    return (a*b)//n


def solution(arr):
    result = arr[0]
    for num in arr[1:]:
        result = gcd(result, num)
    return result


print(solution([2, 6, 8, 14])) #=> 168
print(solution([1, 2, 3])) #=> 6
