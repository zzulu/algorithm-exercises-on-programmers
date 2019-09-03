def solution(n)
    # 1.upto(n).select{|i| n % i == 0}.sum
    (1..n).select{|i| n % i == 0}.sum
end

p solution(12)
p solution(5)
