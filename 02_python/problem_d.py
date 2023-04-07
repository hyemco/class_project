import requests
from pprint import pprint

URL = 'https://api.themoviedb.org/3/search/movie?api_key=d25e6f760f5ccddb631cd3a9b79b03a5&language=ko-KR'


def recommendation(title):
   
    params = {'query': title}
    response = requests.get(URL, params=params).json()
    if response['results'] == []:
        return None
    else:
        movie_id = response['results'][0]['id']

    recommend_URL = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=d25e6f760f5ccddb631cd3a9b79b03a5&language=ko-KR'

    recommend_movies = requests.get(recommend_URL).json()
    target_movie_dict = recommend_movies['results']

    target_movies = [target_movie.get('title') for target_movie in target_movie_dict]

    return target_movies


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
