# requests  

pip(install 관리자)도 LEGB rule을 따름  
* git으로 가상환경을 관리하는 방법을 알아보시오 - 시도해보시오  
python이 있는 위치의 lib/site-packages 내에 install 된다.  
`pip install requests`  

오늘 requsts로 불러올 내용은 [JSON Place Holder](https://jsonplaceholder.typicode.com/todos)  
위 홈페이지의 todos를 사용해 `completed`가 `True`인 `id`, `title`을 불러옴  

추가로, users를 받아와, user의 정보를 남겨서 집어 넣고 싶음  

# CSV  
: comma-separated values = 몇 가지 쉼표로 구분되어 있는 text file  
### 특징
1. 단순한 형식 - 사람이 읽기 쉽고 작성하기 쉬운 형식   
2. 호환성 - 거의 모든 스프레드시트 프로그램 지원  
3. 텍스트 기반 - 텍스트 편집기로 쉽게 편집 가능  

### with statement  
* open 함수  
  * 파일을 열고 파일 객체를 반환하는 함수  
  `open(filename, mode)`  
  encoding도 지정할 수 있음 - encoding을 따로 지정하지 않는 경우: 1. 파일 encoding / 2. OS encoding  

파일을 열고 다 썼으면 다시 닫아줘야 함: 메모리를 생각해서
`data.close()`

* with문의 사용  
with 표현식 as 변수: # alias (별칭) 표현식의 결과값을 변수에 할당  
with문 종료 시, 리소스 해제까지 함께 진행  
: 파일종료뿐 아니라 network 연결 해제까지
아래는 예시  
```python
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
```
아래와 같은 방식으로 csv 파일로부터 dictionary를 만들 수 있음  
```python
with open('users.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    print(csv_reader.fieldnames)
    for row in csv_reader:
        print(row)
```
### CSV file write  
#### newline 매개변수  
* open 함수의 매개변수  
* 파일에서 새로운 줄을 처리하는 방식 지정  
 - None(기본값): 모든 줄바꿈 문자(\n, r\n. \r)를 기본 줄바꿈 문자로 변환  
 - '': 줄바꿈 문자를 변환하지 않음 (raw 모드)  
 - '\n': 줄바꿈 문자를 LF로 변환  -- Linux 환경
 - '\r\n': 줄바꿈 문자를 CRLF (Carriage Return + Line Feed)  
 - '\r': 줄바꿈 문자를 CR 로 변환

=> 맨날 뜨는 CRLF warnings 문제가 이것 때문에 발생한다.  
* 위를 기본값으로 해두고 `csv_write` 첫번째 예시 코드처럼 작성하면 두 번의 줄바꿈이 발생  
=> 해결을 위해서는 `newline` 속성을 이용해야 함  

# 01 PJT  

