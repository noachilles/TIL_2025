### 파이썬 함수의 특징
* def 키워드를 사용하여 정의  
* 일급 객체
  * 함수가 변수에 할당될 수 있음  
  * 함수가 다른 함수의 인자로 전달될 수 있음  
  * 함수가 다른 함수에 의해 반환될 수 있음  
* 익명 함수로 사용 가능 (람다 표현식)  

### 매개변수와 인자  
* 매개변수  
: 함수를 정의할 때 호출 시 받을 값을 저장할 변수    

* 인자  
: 함수를 호출할 때 실제로 전달되는 값  

keyword 인자는 항상 위치 인자 뒤에 와야함  
```python
def greet(name, age):
  print(f'{name}: {age}세')

greet(age = 35, 'Dave') # 안 됨
```  

### Arbitrary Argument Lists (임의의 인자 목록)  
* 정해지지 않은 개수의 인자를 처리하는 인자 - tuple로 넘어감  
* 함수 정의 시 매개변수 앞에 '*'를 붙여 사용하며, 여러 개의 인자를 tuple 처리  

```python
def greet(*args):
```

### Arbitrary Keyword Argument Lists (임의의 키워드 인자 목록)  
* 정해지지 않은 개수의 '키워드' 인자 처리 - dict로 넘어감  
```python
def print_info(**kwargs):
  print(kwargs)  

print_info(name='Dave', age = 25)
```

## 내장 함수  
### map  
: 순회 가능한 데이터구조(iterable)의 모든 요소에 함수를 적용, 그 결과를 map object로 반환  
map obj를 그대로 사용할 수 없고, list 등을 사용해 type conversion을 거쳐야 함  

### zip  
: 임의의 iterable을 모아 '튜플을 원소로 하는' zip obj를 반환  
zip obj 역시 그대로 사용할 수 없고, list 등으로 type conversion 거쳐야 함  
* 여러 개의 리스트를 동시에 조회할 때 활용할 수 있음  
* 2차원 리스트와 같은 컬럼 요소를 동시에 조회할 때 사용할 수 있음  

