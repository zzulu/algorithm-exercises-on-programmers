def solution(arr)
  (arr << arr[0].lcm(arr[1])).shift(2) while arr.size > 1; arr.pop
end

p solution([2,6,8,14])
p solution([1,2,3])
