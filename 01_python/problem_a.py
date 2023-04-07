import json
from pprint import pprint


def movie_info(movie):
    keys = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    movie_info_dict = {}
    for key in keys:
        movie_info_dict[key] = movie[key]
    return movie_info_dict   


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
