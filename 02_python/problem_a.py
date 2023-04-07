import requests

URL = 'https://api.themoviedb.org/3/movie/popular?api_key=d25e6f760f5ccddb631cd3a9b79b03a5&language=ko-KR'


def popular_count():
    response = requests.get(URL).json()
    movies = response['results']
    movies_cnt = len(movies)
    return movies_cnt
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
