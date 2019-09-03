def solution(x)
  x.modulo(x.digits.sum).zero?
end

p solution(10)
p solution(12)
p solution(11)
p solution(13)
