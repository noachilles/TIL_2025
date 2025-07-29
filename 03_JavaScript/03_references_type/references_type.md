# 객체
: 키로 구분된 데이터 집합을 저장하는 자료형  
## 구조 및 속성  
* 중괄호를 이용해 작성  
* 중괄호 안에는 key: value 쌍으로 구성된 속성을 여러 개 작성 가능  
* key는 문자형만 허요  
* value는 모든 자료형 허용  
**function도 value로 넣을 수 있음**  
점('.')으로도 접근할 수 있다  

## 객체와 함수  
### Method  
* 객체 속성에 정의된 함수  
* object.method() 방식으로 호출  

## this
: 함수나 메서드를 '호출한' 객체를 가리키는 키워드  

JS에서 this는 함수를 "호출하는 방법"에 따라 가리키는 대상이 다름  
호출 방법 - 대상  
1. 단순 호출 - 전역 객체  
```javascript
const gr = obj.greeting()
gr()
```
2. 메서드 호출 - 메서드를 호출한 객체  

### 중첩된 함수 - (맥시컬 scope?)  
Ex) forEach의 인자로 작성된 함수는 일반적인 함수 호출 -> this가 전역 객체를 가리킴  
해결책: 화살표 함수는 자신만의 this를 가지지 않기 때문에 외부 함수에서의 this 값을 가져옴  

## 추가 객체 문법

### 1. 단축 속성  
키 이름과 값으로 쓰이는 변수의 이름이 같은 경우, 단축 구문을 사용할 수 있음  
### 2. 단축 메서드  
메서드 선언 시 function 키워드 생략 가능  
### 3. 계산된 속성  
키가 대괄호로 둘러싸여 있는 속성  
고정된 값이 아닌 변수 값을 사용할 수 있음  
### 4. 구조 분해 할당  
배열 또는 객체를 분해해 객체 속성을 변수에 쉽게 할당할 수 있는 문법  
### 5. Object with '전개 구문'  
```javascript
const obj = {b:2, c:3, d:4}
const newObj = {a: 1, ...obj, e:5}

console.log(newObj) // {a:1, b:2, c:3, d:4, e:5}
```


### 7. Optional chaining('?.')  
속성이 없는 중첩 객체를 에러 없이 접근할 수 있는 방법  
만약 참조 대상이 null 또는 undefined라면 에러가 발생하는 것 대신 평가를 멈추고 undefined를 반환  
* 남발하지는 말자~

## 참고  
### JSON  
: "JavaScript Object Notation"  
서로 다른 프로그래밍 언어에서 동일한 데이터를 사용할 수 있도록 해주는 역할  


# 배열  
: Object(객체)에 속함 - 순서가 있는 데이터 집합을 저장하는 자료구조  
length를 변경할 수 있음 - 속성  

## 배열 메서드  
push / pop : 배열 끝 요소 추가 / 제거  
unshift / shift : 배열 앞 요소를 추가 / 제거  

## Affay helper method  
: 배열 조작을 보다 쉽게 수행할 수 있는 특별한 메서드 모음  
* forEach: 배열 내의 모든 요소 각각에 대해 함수를 호출 / 반환 값 X  
* map: 배열 내 모든 요소 각각에 대해 함수를 호출 / 호출 결과 모아 새로운 배열 반환  

### forEach   
```javascript
arr.forEach(callback(item[, index[, array]]))
```  
* 콜백함수는 3가지 매개변수로 구성  
  1. item: 처리할 배열 요소  
  2. index: 처리할 배열 요소 인덱스 (선택 인자)   
  3. array: forEach를 호출한 배열 (선택 인자)  

### map  
* return이 있어 새로운 배열을 만든다는 특징이 있음  

### 기타 Array Helper Methods  
* filter: 콜백 함수의 반환 값이 참인 요소들만 **모아서 새로운 배열을 반환**  
* find: 콜백 함수의 반환 값이 참이면 해당 요소를 반환 - **최초로 찾은 하나의 값을 반환** 
* reduce(): 배열의 모든 요소를 누적해서 하나의 값으로 줄이는 데 적합한 메서드  
  `(sum, num) => sum + num` 은 각 요소를 누적하는 콜백  


## 추가 배열 문법  
```javascript
arr = [1, 2, 3]
arr[-1] = 4
console.log(arr) // [1, 2, 3, -1: 4]
```  

### 추가 문법  
```javascript
console.log("3" + 3) // '33'
console.log("2" - 1) // 1
```
