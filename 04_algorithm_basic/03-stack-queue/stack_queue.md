# Stack  
## 스택의 구조와 작동 원리  
## 스택 응용  
### 응용 1. 괄호 검사  
전체 문장의 한 글자씩 순회하면서 -> 여는 괄호만 스택에 넣음  
닫는 거 나오면 맨 마지막에 들어있는 괄호 스타일이 어떤 것인지 확인하고, 만약 현재 확인 중인 괄호와 같다면 pop()

### 응용 2. function call

### 응용 3. 계산기  
: 문자열로 된 계산식이 주어질 때, 스택을 이용해 계산식의 값을 계산 가능  


# Queue
## 큐의 구조와 작동 원리  
### 큐  
* 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조  
* 선입선출 구조  
만약, 스택과 같이 list의 `pop()`을 사용하려고 하면 시간복잡도가 `O(N)`  
따라서, `from collections import deque`를 활용한다.  

```python
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
```
deque에서는 `popleft()`의 시간복잡도가 `O(1)`  

* 스택과의 정말 중요한 차이점: 입구와 출구가 다르다 => front와 rear의 2개의 인덱스를 이용함  

리스트를 사용하면 queue를 구현할 때 `is_empty()` 함수 사용 등에서 문제가 발생함  
이걸 해결하기 위해서 Circular Queue를 구현함  

하지만, 이런 Circular Queue를 직접 구현하기는 힘들고, 리스트의 한계를 보완하고 싶을 때: 연결 리스트(Linked List)를 사용함  

## 연결 리스트  
### 단순 연결 리스트 (Singly Linked List)  
: 다음 노드 자체를 가리키도록 한다.  
Head에 저장된 참조값을 새로운 노드 new의 링크 필드값에 저장한다.  
Head에 새로운 노드 new의 참조값을 저장한다.  
* Linked List가 Full한지는 물어보지 않아도 된다. -> 그냥 추가하면 되므로