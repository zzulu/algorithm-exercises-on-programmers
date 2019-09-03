def solution(n)
  (2..n).each_with_object([0,1]){|i, arr|arr << arr.sum; arr.shift}.last % 1234567
end

p solution(3)
p solution(5)
p solution(100000)
