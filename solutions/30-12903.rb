def solution(s)
    q, r = s.size.divmod(2)
    s[q-1+r..q]
end

puts solution('abcde')
puts solution('qwer')

