# 외부 라이브러리 requests를 impprt
import requests
from pprint import pprint # pretty print

# 오늘 수업에서는 Json Place holder를 사용: Java Script 형식
# placeholder 어디서 들어봤다 했더니 html input 항목에 기본적으로 입력되어 있는 것을 placeholder라 함  
response = requests.get('https://jsonplaceholder.typicode.com/todos').json()
user_response = requests.get('https://jsonplaceholder.typicode.com/users').json()

# 출력하면 어떤 응답을 받았는지 보여줌(내용 X, 정상적으로 받았는지)
# 200번대는 정상 응답
# print(response) # <Response [200]>

# requests: get 요청으로 응답 받은 데이터를 담은 객체에 json()이라는 메서드 만들어둠  
# => JS 형식의 JSON 데이터를 파이썬에서 활용할 수 있도록 & python 타입에 맞게 변환해줌
# print(response.json()) # 데이터가 출력됨

completed_todos = [] # 최종 결과물을 담을 리스트
fields = ['id', 'title']

for item in response:
    # completed 요소가 True인 값만 출력하는 방법 두 가지
    # if item['completed'] == True:
    #     print(item)
    if item.get('completed'):
        # 그중, 내가 필요로 하는 2개의 필드인 id, title만 따로 모음
        temp_item  = {}
        for key in fields: # 'id', 'title'
            # temp_item['id'] = item['id'] value
            temp_item[key] = item[key]
            # {'id': 1, 'title': 'delectus aut autem' \n ...}

        for user in user_response:
            if user['id'] == item['userId']:
                # ctrl + alt + 위아래 방향키: 여러 줄
                # ctrl + shift + 좌우 방향키: 단어 단위 드래그
                user_info = {
                    'id': user['id'],
                    'name': user['name'],
                    'username': user['username'],
                    'email': user['email'],
                }
                temp_item['user'] = user_info

        # 어떻게 이 반복문을 더 줄일 수 있을까?

        completed_todos.append(temp_item)
pprint(completed_todos)

