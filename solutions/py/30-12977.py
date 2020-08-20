def is_prime(n):
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    else:
        return True


def solution(nums):
    count = 0
    l = len(nums)
    for i in range(l):
        for j in range(i+1, l):
            for k in range(j+1, l):
                if is_prime(nums[i] + nums[j] + nums[k]):
                    count += 1
    return count


print(solution([1, 2, 3, 4])) #=> 1
print(solution([1, 2, 7, 6, 4])) #=> 4
