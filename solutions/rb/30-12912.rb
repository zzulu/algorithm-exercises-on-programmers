def solution(a, b)
    a,b = b,a if a > b
    return (a..b).to_a.inject(&:+)
end

p solution(3,5)
