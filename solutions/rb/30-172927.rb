def solution(picks, minerals)
  result = 0
  fatigue = [
    { diamond: 1, iron: 1, stone: 1 },
    { diamond: 5, iron: 1, stone: 1 },
    { diamond: 25, iron: 5, stone: 1 },
  ]

  calculated_fatigue = []

  minerals = minerals[0..(5*picks.sum)]

  mineral_index = 0
  while mineral_index < minerals.size
    pick_limit = 5
    with_diamond, with_iron, with_stone = 0, 0, 0
    until pick_limit == 0
      with_diamond += fatigue[0][minerals[mineral_index].to_sym]
      with_iron += fatigue[1][minerals[mineral_index].to_sym]
      with_stone += fatigue[2][minerals[mineral_index].to_sym]
      pick_limit -= 1

      mineral_index += 1
      if mineral_index >= minerals.size
        break
      end
    end
    calculated_fatigue.push([with_diamond, with_iron, with_stone])
  end

  calculated_fatigue.sort_by! do |item|
    [item[2], item[1], item[0]]
  end

  picks.each_with_index do |pick_count, pick|
    pick_count.times do
      unless calculated_fatigue.empty?
        result += calculated_fatigue.pop[pick]
      else
        return result
      end
    end
  end

  return result
end


p solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]) #=> 12
p solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]) #=> 50
