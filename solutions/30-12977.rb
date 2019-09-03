require 'prime'

def solution(nums)
  nums.combination(3).map{|a| a.sum}.map{|n| Prime.prime?(n)}.count(true)
end

p solution([1,2,3,4])
p solution([1,2,7,6,4])
