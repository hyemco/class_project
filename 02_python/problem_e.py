import requests
from pprint import pprint

search_URL = 'https://api.themoviedb.org/3/search/movie?api_key=d25e6f760f5ccddb631cd3a9b79b03a5&language=ko-KR'

def credits(title):
    params = {'query': title}
    response = requests.get(search_URL, params=params).json()

    if response['results'] == []:
        return None
    else:
        movie_id = response['results'][0]['id']

    credists_URL = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=d25e6f760f5ccddb631cd3a9b79b03a5&language=ko-KR'
    credits = requests.get(credists_URL).json()
    cast_list = {'cast': [], 'directing' : []}
    for cast in credits['cast']:
        if cast['cast_id'] < 10:
            cast_list['cast'].append(cast['name'])
    for crew in credits['crew']:
        if crew['department'] == 'Directing':
            cast_list['directing'].append(crew['name'])

    return cast_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
