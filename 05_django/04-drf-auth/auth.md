# Cookie & Session  
브라우저가 쿠키도 웹페이지와 함께 보내줌  

* 개발자 도구 - Network 탭 - cartView.pang 확인  

## 쿠키 사용 목적  
1. 세선 관리  
  - 로그인, 아이디 자동완성, 공지 하루 안 보기, 팝업 체크 장바구니 등의 정보 관리  

2. 개인화  
  - 사용자 선호, 테마 등의 설정  

3. 트래킹  
  - 사용자 행동을 기록 및 분석  

=> 자리 이동할 때 세션, 쿠키를 모두 삭제하면 컴퓨터 비워짐  

## 세션 작동 원리  

1. client: login => server: session 생성 후 저장  
2. 생성된 session 데이터에 인증할 수 있는 session id 발급  
3. 발급한 session id를 client에 응답  
4. 클라이언트는 응답 받은 session id를 쿠키에 저장  
5. client가 다시 동일한 서버에 접속: 요청과 함께 쿠키를 서버에 전달  
6. 쿠키는 요청 때마다 서버에 함께 전송됨  

주기적으로 DB의 세션 id를 삭제해준다  
=> 내 PC에 물리적으로 저장되어 있어도, 서버는 새로 인증을 요청  
: 은행 / swea 등에선 시간따라서 로그인 갱신 요청  
=> 로그인 갱신을 하면 새로운 세션 id 발급  

세션 기반 인증 확인 - 되도록 accounts로 만들기를 권장  

## 쿠키와 세션의 목적  
: 서버와 클라이언트 간 '상태'를 유지  
-> 토큰을 사용해야 하는 이유로 연결됨 - 세션id를 로그인 할 때마다 쓰면 번거롭고 불편하므로

# 인증과 권한  
순서상 인증이 먼저 진행 -> 수신 요청을 해당 요청의 사용자 or 해당 요청이 서명된 토큰과 같은 자격 증명 자료와 연결  
권한 및 제한 정책: 인증 완료된 해당 자격 증명 사용해 요청 허용 여부 결정  

* 인증은 인증만. 들어오는 요청을 허용 / 거부할 수 없음  
**단순히 요청에 사용된 자격 증명만 식별**한다는 점에 유의  

## 응답 종류  
1. HTTP 401: 유효한 자격 증명이 X  
2. HTTP 403: 권한 떄문에 거절됨 - 서버는 클라이언트가 누구인지는 알고 있음  

## 인증 체계 설정 방법 2가지  
1. 전역 설정  
2. View 함수별 설정  

dj-rest-auth를 사용해서 설정하고, dj-rest-auth가 login에 필요한 기능을 인증해줌  
Token을 기본으로 사용하면, session_id를 받은 것이 아니라 `{key: "key"}` 형식으로 반환됨  

## 토큰 적용  

POST로 api/v1/articles/에서 게시글을 작성할 때  
body는 게시글 정보를 저장하는 곳,  
headers에  
`{Authorization: Token <Token>}` 해당 양식으로 넘겨주면 됨  

로그인 정보를 받아서 토큰을 생성하는 것까지는 dj-rest-auth에 맡겼고  
인증받은 토큰 정보를 토대로 request.user라는 정보를 바탕으로 어느user인지를 알아낸다.  

dj-rest-auth를 사용하면서 다른 기능들이 필요하지는 않지만 accounts 앱을 만드는 것이 필요하다 - 나중에 custom 할 수도 있으므로  

인증을 모두 한 다음 권한을 설정해주어야 함  

## 권한 체계 설정 방법 2가지  
1. 전역 설정 - 일단 다 허용: default 값  
2. View 함수별 설정  

```python
# articles/views.py

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ...
```
올바르게 인증된 유저인지를 확인해서 -> isauthenticated 해야지 전체 조회 가능  

dj-rest-auth는 회원가입에 대한 기능도 기본적으로 제공해줌 - 보통은 제공하지 X  

django-allauth의 버전이 기능에 영향을 주기 때문에, 이걸 신경써야 함  

외부 framework를 사용하면 - 어떤 식으로?: 이 불편한 이슈가 왜 일어났는지 찾아보기~  