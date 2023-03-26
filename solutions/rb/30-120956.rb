def solution(babbling)
  count = 0
  able = ['aya', 'ye', 'woo', 'ma']
  babbling.each do |word|
    able.each do |a|
      word.sub!(a, ' ')
    end
    if word.strip.empty?
      count += 1
    end
  end
  return count
end


p solution(["aya", "yee", "u", "maa", "wyeoo"]) #=> 1
p solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]) #=> 3

