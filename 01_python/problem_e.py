import json


def dec_movies(movies):
    release_in_12_list = []

    for movie in movies:
        detail_info = open('data/movies/' + str(movie['id']) + '.json', encoding='utf-8')
        detail_info_list = json.load(detail_info)

        if int(detail_info_list['release_date'].split('-')[1]) == 12:
            release_in_12_list.append(detail_info_list['title'])
    
    return release_in_12_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
