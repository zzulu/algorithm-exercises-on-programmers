def solution(n)
  (n.next..Float::INFINITY).detect{|i| i.to_s(2).count('1') ==  n.to_s(2).count('1')}
end

p solution(78)
p solution(15)
