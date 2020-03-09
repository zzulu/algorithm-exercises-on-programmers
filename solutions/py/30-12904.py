def solution(s):
    length = len(s)
    for l in range(length, 0, -1):
        for start in range(length-l+1):
            for i in range(l//2):
                if s[start+i] != s[start+l-1-i]:
                    break
            else:
                return l


print(solution('abcdcba')) # 7
print(solution('abacde')) # 3
print(solution('abcbae')) # 5
print(solution('abcde')) # 1
