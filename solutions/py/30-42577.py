def solution(phone_book):
    phone_book.sort(key=lambda p: len(p))

    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book[i:])):
            for k in range(len(phone_book[i])):
                if phone_book[i][k] != phone_book[j][k]:
                    break
            else:
                return False
    else:
        return True


print(solution(['119', '97674223', '1195524421'])) #=> false
print(solution(['123', '456', '789'])) #=> true
print(solution(['12', '123', '1235', '567', '88'])) #=> false
