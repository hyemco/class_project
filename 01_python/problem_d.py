import json


def max_revenue(movies):
    max_revenue_val = 0

    for movie in movies:
        detail_info = open('data/movies/' + str(movie['id']) + '.json', encoding='utf-8')
        detail_info_list = json.load(detail_info)

        if max_revenue_val < detail_info_list['revenue']:
            max_revenue_val = detail_info_list['revenue']
            max_revenue_title = detail_info_list['title']

    return max_revenue_title

        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
