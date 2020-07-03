# Python:: 해시, 셋 사용방법

<br>

## 해시 개념 및 사용방법
---
### Python의 Hash는 Dictionary
Dictionary는 기본으로 dict 클래스에 구현되어있다. 

### 해시는 언제 사용해야하는가.
- 데이터의 중복이 없어도 될 때 : 집합의 모든 데이터는 유일함. 동일 원소를 제거할 때 사용하자.
- 빠른 접근 / 탐색이 필요할 때 : 딕셔너리는 대부분의 시간복잡도가 O(1)로 탐색이 매우 빠른 자료구조임
- 집계를 할때 : 코딩테스트에서는 각 원소의 개수를 세야하는 문제가 많이 나온다. 이때 사용하기 유용함! (collections의 모듈 Counter 클래스!!)

### Dictionary와 리스트의 시간 복잡도 비교

| Operation | Dictionary | List |
| --- | :---: | ---:|
| Get Item | O(1) | O(1) |
| Insert Item | O(1) | O(1) ~ O(N) |
| Update Item | O(1) | O(1) |
| Delete Item | O(1) | O(1) ~ O(N) |
| Search Item | O(1) | O(N) |


- #### Dictionary :: init
    ```python
    dict1 = {} 
    dict2 = dict()
    dict3 = {'name' = 'a', 'age' = 60}
    dict4 = {'countries': {'capital':'seoul','continent':'Asia'}}
    ```
- #### Dictionary :: Get
    딕셔너리 원소를 가져올 때는 1)[] 2)get(key, x) 메소드를 사용한다.
    1) 방법의 경우 딕셔너리에 key가 없으면 keyerror가 발생함
    2) 의 경우 key가 없으면 x를 반환한다.
    ```python
    my_dict.get('name', '홍길동')
    ```

- #### Dictionary :: Set
    딕셔너리에 값을 집어넣거나 업데이트 시 [key]를 사용한다.
    ```python
    my_dict['name'] = '에이미'
    my_dict['age'] += 30
    ```

- #### Dictionary :: Delete
    딕셔너리에 특정 key값을 지우려면
    1) del dict1[key] (key가 없으면 keyerror)
    2) dict1.pop(key, default_value) (key가 없으면 default_value 리턴)
    ```python
    del my_dict['김철수']
    my_dict.pop('김철수', 100)
    ```

- #### Dictionary :: Iterate
    ```python
    for key in my_dict:
        print(key, my_dict[key]) #key만 조회
    
    for key, value in my_dict.items():
        print(key, value) #key와 value 같이 조회
    print(my_dict.keys()) #key만 뽑아냄
    print(my_dict.values()) #값만 뽑아냄
    print(my_dict.items()) #key, value를 튜플로 뽑아냄
    ```

- #### Dictionary :: 집계를 위한 클래스 collections Counter class
    문제를 풀다보면 어떤 원소 x가 몇번 등장하는지 셀 필요성이 있음
    ```python
    from collections import Counter
    my_list = ["박수진", "박수진", "홍길동", "김철수", "김철수"]
    my_counter = Counter(my_list)
    my_counter['박수진']
    dict(my_counter)
    ```
<br>
<br>

## 집합 개념 및 사용방법
---
### Python의 집합은 Set
### 집합은 언제 사용해야하는가.
- 리스트를 사용할 수 없을 때 : 원소에 접근하는 요소가 숫자 인덱스가 아닌 문자열이나 튜플일때, 사용한다.
- 다루는 데이터의 삽입/삭제/탐색 이 자주 일어날 때 (데이터가 정수가 아닐 때) : 문자열 등 리스트가 index로 활용하지 못하는 데이터를 빠르게 탐색할 때 매우 유용함. O(1) 소요
- 수학적으로 교집합/합집합/차집합을 구할 때 : 파이썬의 set은 수학 집합의 대부분의 기능을 수행한다.


### set와 리스트의 시간 복잡도 비교

| Operation | Dictionary | List |
| --- | :---: | ---:|
| 탐색 | O(1) | "abc" in my_set |
| 제거 | O(1) | my_set.remove("abc") |
| 합집합 | O(len(set1) + len(set2)) | my_set1 | my_set2 |
| 교집합 | O(min(len(set1), len(set2))) | my_set1 & my_set2 |
| 차집합 | O(len(set1)) | my_set1 - my_set2 |
| 합집합 - 교집합 | O(len(set1)) | my_set1 ^ my_set2 |

### 집합의 주의사항
hashable한 타입만 집합에 넣을 수 있다. list, dict, set 유저 클래스 사용 불가능, tuple은 삽입 가능!
     
- #### Set :: init
    ```python
    empty_set = set()
    my_set = set([1,2,3,4])
    ```
- #### Set :: add
    ```python
    my_set.add('demi')
    ```

- #### Set :: delete
    ```python
    my_set.remove('demi')
    ```

- #### Set :: 집합
    ```python
    set1 = set([1,2,3,4,5])
    set2 = set([3,4,5,6,7])
    f_set = set1 | set2
    s_set = set1 & set2
    t_set = set1 - set2
    ```
<br>
<br>
