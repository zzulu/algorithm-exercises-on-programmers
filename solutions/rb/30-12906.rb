def solution(arr)
  arr.join('').squeeze.split('').map(&:to_i)
end

p solution([1,1,3,3,0,1,1])
