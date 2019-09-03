def solution(n)
  n.even? ? '수박'*(n/2) : '수박'*(n/2)+'수'

  # ['수박','수'].zip(n.divmod(2)).map{|x, y| x * y}.join
end

p solution(3)
p solution(4)
