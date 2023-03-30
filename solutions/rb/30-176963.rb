def solution(name, yearning, photo)
  score = Hash[(0...name.length).collect { |i| [name[i], yearning[i]] }]

  answer = photo.collect do |item|
    item.inject(0) do |sum, n|
      sum + (score[n] || 0)
    end
  end

  return answer
end


p solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])
#=> [19, 15, 6]
p solution(["kali", "mari", "don"], [11, 1, 55], [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]])
#=> [67, 0, 55]
p solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may"],["kein", "deny", "may"], ["kon", "coni"]])
#=> [5, 15, 0]
