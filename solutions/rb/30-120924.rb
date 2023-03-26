def solution(common)
  numbers = common[-3..-1]

  d1 = numbers[1] - numbers[0]
  d2 = numbers[2] - numbers[1]
  if d1 == d2
    return numbers[2] + d1
  else
    r = d2 / d1
    return numbers[2] * r
  end
end


p solution([1, 2, 3, 4]) #=> 5
p solution([2, 4, 8]) #=> 16
