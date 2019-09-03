def solution(arr)
  arr.delete(arr.min); arr.empty? ? [-1] : arr
end

p solution([4,3,2,1])
p solution([10])
