def solution(park, routes)
  y, x = nil, nil
  max_y, max_x = park.length, park[0].length
  board = park.each_with_index.map do |r, start_y|
    row = r.split('')
    if y.nil? and x.nil?
      start_x = row.index('S')
      unless start_x.nil?
        y, x = start_y, start_x
      end
    end
    next row
  end

  directions = {
    N: [-1, 0],
    E: [0, 1],
    S: [1, 0],
    W: [0, -1],
  }

  routes.each do |route|
    point, step = route.split
    dy, dx = directions[point.to_sym]

    can_move = true
    (1..step.to_i).each do |s|
      new_y = y+(dy*s)
      new_x = x+(dx*s)

      if new_y < 0 or new_x < 0 or new_y >= max_y or new_x >= max_x
        can_move = false
        break
      end

      position = park[new_y][new_x]
      if position.nil? or position == 'X'
        can_move = false
        break
      end
    end

    if can_move
      y += dy*step.to_i
      x += dx*step.to_i
    end
  end

  return [y, x]
end


p(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"])) #=> [2,1]
p(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"])) #=> [0,1]
p(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"])) #=> [0,0]

p(solution(["OSO","OOO","OOO","OOO"], ["S 5"])) #=> [0,1]
p(solution(["OSO","OOO","OOO","OOO"], ["E 5"])) #=> [0,1]

p(solution(["XXX","XSX","XXX"], ["E 1"])) #=> [1,1]

p(solution(["OOXOS","OOOOO","OOOOO", "OOOOO", "OOOOO"], ["W 3"])) #=> [0,4]
p(solution(["SOXOO","OOOOO","OOOOO", "OOOOO", "OOOOO"], ["E 3"])) #=> [0,0]
