import requests

search_URL = 'https://api.themoviedb.org/3/search/movie?api_key=d25e6f760f5ccddb631cd3a9b79b03a5&language=ko-KR'

def get_poster_url(title):
    global poster_url
    params = {'query': title}
    response = requests.get(search_URL, params=params).json()

    if response['results'] == []:
        return None
    else:
        movie_id = response['results'][0]['id']
        poster_URL = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=d25e6f760f5ccddb631cd3a9b79b03a5&language=ko-KR'
        poster_url = requests.get(poster_URL).json()
    return poster_url['poster_path']