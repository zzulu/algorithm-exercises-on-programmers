def solution(w,h):
    area = w * h
    q, r = (h, w) if h > w else (w, h)

    while q % r:
        q, r = r, q % r

    return area - (w + h - r)


print(solution(8, 12)) #=> 80
