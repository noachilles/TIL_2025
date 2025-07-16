# Command Line Interface
: 명령어를 통해 사용자와 컴퓨터가 상호작용하는 방식  

## CLI 문법 및 활용

CLI에서 '.'의 역할  
'.' :현재 디렉토리
'..' : 현재의 상위 디렉토리(부모 폴더)  

### CLI 기초 문법  
---

**touch**: 파일 생성
```bash
$ touch some_file.txt
```  
> 공백을 쓰지 않는 이유 : if `touch some file.txt` 를 사용하면 some / file 2개의 파일이 생성되기 때문이다.  

**mkdir X** : 새 디렉토리 생성 
```bash
$ mkdir X # 현재 디렉토리에 이름이 X인 새로운 디렉토리 생성
```

**ls** : 현재 작업 중인 디렉토리 내부의 폴더 / 파일 목록 출력  
```bash
$ ls -a # 여기서 a는 all : 숨김 파일까지 표시한다
$ ls -l # l은 list : 리스트 형식으로 보여줌
```  

**cd(change directory)** : 현재 작업 중인 디렉토리를 변경 (위치 이동)
```bash
$ cd .. # 상위 폴더로 이동
$ cd 02_git_adv # 현재 폴더 내부의 폴더로 이동
$ cd ../01_git # 동일한 부모 폴더 내부 다른 폴더로 이동 = 즉, 형제 폴더
$ cd ../.. # 상위 폴더의 상위 폴더로 이동
```  

**start** : 폴더 / 파일을 열기  
```bash
$ start some_file.txt # 특정 파일을 열어줌 
$ start . # 현재 폴더를 열어줌
```

**rm** : 파일 삭제 & 디렉토리 파일은 -r 옵션 추가 사용  
**복구 못함! 진짜 지워도 되는지 두 번 생각하고 사용합시다**  
  공백으로 여러 개 삭제 가능
```bash
$ rm some_fime.txt # 파일 삭제 예시
$ rm -r X # r은 recursion - 폴더 삭제
```  

### 절대 경로와 상대 경로
---
**절대 경로**   
: Root 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것  
Ex) 'C:\Users\SSAFY\Desktop'  

Window: 슬래시를 사용한다.

**상대 경로**  
: 현재 작업하고 있는 디렉토리 기준으로 계산된 상대적 위치를 작성한 것  
만약 현재 작업 디렉토리가 'C:/Users'일 때,
윈도우 바탕 화면의 상대 경로는 'SSAFY/Desktop'  

