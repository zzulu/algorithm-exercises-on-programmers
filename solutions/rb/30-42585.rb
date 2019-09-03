def solution(arrangement)
  stack = ['(']
  arrangement.split(//).each_cons(2).inject(0) do |piece, (prev, curr)|
    if curr == '('
      stack.push(curr)
      piece += 0
    else
      stack.pop
      prev == ')' ? piece += 1 : piece += stack.size
    end
  end
end

p solution('()(((()())(())()))(())') #=> 17
p solution('(())') #=> 2
p solution('()') #=> 0
