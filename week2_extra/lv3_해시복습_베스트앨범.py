def solution(genres, plays):
    answer = []
    music_dict = {}

    for i, genre in enumerate(genres):
        music_dict[genre] = music_dict.get(genre, [[0, -1]])
        music_dict[genre].append((plays[i],i))
        music_dict[genre][0][0] += plays[i]
        
    for key, value in sorted(music_dict.items(), key = lambda item:-item[1][0][0]): 
        value.sort(key = lambda x: -x[0])
        answer.append(value[1][1])
        if len(value)>2:
            answer.append(value[2][1])
    
    return answer