def solution(participant, completion):
    dp = {}
    for p in participant:
        dp[p] = dp[p] + 1 if p in dp else 1
    
    for c in completion:
        dp[c] -= 1
    
    for p, count in dp.items():
        if count:
            return p


print(solution(['leo', 'kiki', 'eden'], ['eden', 'kiki'])) #=> 'leo'
print(solution(['marina', 'josipa', 'nikola', 'vinko', 'filipa'], ['josipa', 'filipa', 'marina', 'nikola'])) #=> 'vinko'
print(solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav'])) #=> 'mislav'
