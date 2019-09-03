def solution(arr, divisor)
    answer = arr.select{|n| n%divisor == 0}.compact.sort()
    answer.empty? ? [-1] : answer
end

p solution([2, 36, 1, 3],1)
