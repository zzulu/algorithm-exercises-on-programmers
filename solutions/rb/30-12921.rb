require 'prime'

def solution(n)
  Prime.each(n).count
end

p solution(10)
p solution(5)
