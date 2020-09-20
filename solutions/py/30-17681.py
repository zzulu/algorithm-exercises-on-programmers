def solution(n, arr1, arr2):
    result = []
    for index in range(n):
        merged, line1, line2 = '', '', ''
        num1, num2 = arr1[index], arr2[index]
        for _ in range(n):
            num1, r1 = num1 // 2, num1 % 2
            line1 = '#' + line1 if r1 else ' ' + line1

            num2, r2 = num2 // 2, num2 % 2
            line2 = '#' + line2 if r2 else ' ' + line2

        for i in range(n):
            merged += '#' if line1[i] == '#' or line2[i] == '#' else ' '

        result.append(merged)

    return result


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])) #=> ["#####","# # #", "### #", "# ##", "#####"]
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])) #=> ["######", "### #", "## ##", " #### ", " #####", "### # "]
