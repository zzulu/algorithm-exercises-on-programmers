def solution(n)
    n.digits.sort.reverse.join.to_i
end

p solution(118372)
