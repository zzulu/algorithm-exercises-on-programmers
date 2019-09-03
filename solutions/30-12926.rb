def solution(s, n)
  s.split(/ /,-1).map {|w| w.chars.map {|c| (c.ord+n > (/[[:upper:]]/.match(c) ? 90 : 122) ? c.ord+n-26 : c.ord+n).chr("UTF-8") }.join}.join(' ')
end

p solution('AB', 1)
p solution('z', 1)
p solution(' a  B z ', 4)
