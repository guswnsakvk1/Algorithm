def solution(genres, plays):
    answer = []
    genreslst = {}
    playslst = {genre : {} for genre in list(set(genres))}
    
    for i in range(len(genres)):
        if genres[i] in genreslst:
            genreslst[genres[i]] += plays[i]
        else:
            genreslst[genres[i]] = plays[i]
            
        playslst[genres[i]].setdefault(i, plays[i])
    
    for genre in sorted(genreslst.items(), key=lambda x: x[1], reverse=True):
        genre_sort_list = sorted(playslst[genre[0]].items(), key=lambda x: x[1], reverse=True)
        if(len(genre_sort_list)) >= 2:
            answer.append(genre_sort_list[0][0])
            answer.append(genre_sort_list[1][0])
        else:
            answer.append(genre_sort_list[0][0])

    return answer