def solution(genres, plays):
    songs = {}
    for i in range(len(genres)):
        if songs.get(genres[i]):
            songs[genres[i]].append((i, plays[i]))
        else:
            songs[genres[i]] = [(i, plays[i])]

    songs = {k: sorted(v, key=lambda v: v[1], reverse=True) for k, v in sorted(songs.items(), key=lambda item: sum([song[1] for song in item[1]]), reverse=True)}

    album = []
    for song in songs.values():
        album += [song[0] for song in song[:2]]

    return album


print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500])) #=>  [4, 1, 3, 0]
