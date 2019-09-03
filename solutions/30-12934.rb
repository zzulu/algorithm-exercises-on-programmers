def solution(n)
  Math.sqrt(n).modulo(1).zero? ? Math.sqrt(n).to_i.next**2 : -1
end

p solution(121)
p solution(3)
