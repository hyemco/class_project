# pjt_02

## problem_a & problem_b
- API와 통신하는 방법, API 문서 보는법을 익힘

## problem_c
- 리스트 안의 딕셔너리의 특정값을 기준으로 정렬할 때 람다 함수를 활용해서 정렬을 함
- 배우고 나서 잘 사용하지 못했던 람다 함수를 써먹어서 좋았음

## problem_d & problem_e
- URL에 쿼리 추가하는 방법을 익힘
    ```
    params = {'key': 'value'} # 딕셔너리 형태로 넣기
    response = requests.get(URL, params=params).json()
    ```
- 데이터를 받아온 후 딕셔너리 형태인지, 리스트에 담겨있는지를 잘 확인하면서 코드를 짜야겠다고 느낌