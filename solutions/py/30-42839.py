from itertools import permutations 


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    else:
        return True


def solution(numbers):
    numbers = [number for number in numbers]
    
    p = []
    for n in range(len(numbers)):
        for n in permutations(numbers, n+1):
            num = int(''.join(n))
            if num not in p and is_prime(num):
                p.append(num)

    return len(p)


print(solution('17')) #=> 3
print(solution('011')) #=> 2
