def solution(n, words)
  if detected = words.each_cons(2).to_a.detect.with_index(1){|(prev, curr), i| words[0..i].count(curr) > 1 || prev[-1] != curr[0] }
    answer = words.rindex(detected[-1]).divmod(n).collect{|v|v+=1}.reverse
  end
  return answer || [0,0]
end

p solution(3,%w(tank kick know wheel land dream mother robot tank))
p solution(5,%w(hello observe effect take either recognize encourage ensure establish hang gather refer reference estimate executive))
p solution(2,%w(hello one even never now world draw))
