def solution(s)
  result, x_count, not_x_count = 0, 0, 0
  x = nil
  s.each_char do |c|
    if x.nil?
      x = c
      x_count += 1
      next
    end

    if x == c
      x_count += 1
    else
      not_x_count += 1
    end

    if x_count == not_x_count
      result += 1
      x_count, not_x_count = 0, 0
      x = nil
    end
  end

  unless x.nil?
    result += 1
  end

  return result
end


p solution('banana') #=> 3
p solution('abracadabra') #=> 6
p solution('aaabbaccccabba') #=> 3
