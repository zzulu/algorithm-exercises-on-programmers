def solution(s)
  s.split(/ /,-1).map{|w| w.chars.each_with_index.map{|c,i| i.even? ? c.upcase : c.downcase}.join}.join(' ')
end

p solution('  try hello  world  ')
