def solution(heights)
  heights.each_with_index.inject([]) {|arr,(h,i)| arr << (heights[0..i].rindex{|t| t > h} || -1) + 1}
end

p solution([6,9,5,7,4])
