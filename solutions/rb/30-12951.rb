def solution(s)
  s.split(/ /,-1).map(&:capitalize).join(' ')
end

p solution("3people unFollowed me")
p solution("for the last week")
