def solution(phone_number)
  phone_number.gsub(/\d(?=\d{4})/,'*')
end

p solution('01033334444')
p solution('027778888')
