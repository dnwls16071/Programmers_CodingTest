def solution(genres, plays):
    # 베스트 앨범에 들어갈 노래의 고유 번호를 저장할 배열 answer
    answer = []
    # 각 장르의 고유 번호와 재생 횟수를 저장할 해시
    genre_dictionary = {}
    for i in range(len(genres)):
        genre_name = genres[i]       # 장르 이름
        music_count = plays[i]      # 재생 횟수
        if genres[i] not in genre_dictionary:   
            genre_dictionary[genres[i]] = [[i, plays[i]]]
        else:
            genre_dictionary[genres[i]].append([i, plays[i]])
    
    # 속한 노래가 많이 재생된 장르를 먼저 수록하므로
    # 각 장르별 재생횟수의 총합을 저장할 해시
    genre_count_dictionary = {}
    for i in range(len(genres)):
        if genres[i] not in genre_count_dictionary:
            genre_count_dictionary[genres[i]] = plays[i]
        else:
            genre_count_dictionary[genres[i]] += plays[i]
    # 많이 재생된 장르를 내림차순으로 정렬
    genre_count_list = sorted(genre_count_dictionary.keys(), key = lambda x : -genre_count_dictionary[x])
    
    # 정렬된 장르별로 노래를 선택합니다.
    for genre in genre_count_list:
        songs = genre_dictionary[genre]
        # 노래를 재생 횟수에 따라 내림차순으로 정렬하고, 고유 번호가 낮은 순으로 정렬합니다.
        songs = sorted(songs, key=lambda x: (x[1], -x[0]), reverse=True)
        # 각 장르에서 최대 2개의 노래를 선택합니다.
        songs = songs[:2]
        for song in songs:
            # 고유번호 저장
            answer.append(song[0])
    return answer