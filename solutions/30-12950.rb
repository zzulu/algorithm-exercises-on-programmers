def solution(arr1, arr2)
  arr1.zip(arr2).map{|a| a.first.zip(a.last).map(&:sum)}
end

p solution([[1,2],[2,3]],[[3,4],[5,6]])
