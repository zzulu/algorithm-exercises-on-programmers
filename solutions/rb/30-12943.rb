def solution(num)
  num == 1 ? 0 : (1..500).detect{|i| (num = num.even? ? num/2 : (num*3)+1) && num == 1 } || -1
end

p solution(6)
p solution(16)
p solution(626331)
p solution(1)
