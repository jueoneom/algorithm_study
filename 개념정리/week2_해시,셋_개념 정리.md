# Python:: 해시, 셋 사용방법

<br>

## 해시 개념 및 사용방법
---
### Python의 Hash는 Dictionary
Dictionary는 기본으로 dict 클래스에 구현되어있다. 

### 해시는 언제 사용해야하는가.
- 리스트를 사용할 수 없을 때 : 원소에 접근하는 요소가 숫자 인덱스가 아닌 문자열이나 튜플일때, 사용한다.
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


- #### deque의 초기화
    ```python
    from collections import deque 
    queue1 = deque() #빈큐 만들기
    queue2 = deque([1, 2, 3]) #원소가 있는 큐 만들기
    queue3 = deque(maxlen = 5) #최대 길이가 명시된 큐 만들기 ( maxlen에 도달시 그 후에 넣는 값은 pop->새값이 채워지는 구조)
    ```
- #### deque :: push 연산
    ```python
    from collections import deque 
    my_deque = deque()
    my_deque.append(3)
    print(len(my_deque))
    ```
- #### deque :: pop 연산
    ```python
    from collections import deque 
    my_deque = deque([1,2,3])
    while my_deque:
        my_deque.popleft()
    ```
- #### deque :: clear
    ```python
    from collections import deque 
    my_deque = deque([1,2,3])
    my_deque.clear()
    ```
<br>
<br>

## 힙 개념 및 사용방법
---
### heap
heap은 데이터가 지속적으로 정렬되어야 하며, 데이터의 삽입, 삭제가 빈번하게 일어날 때 사용하는 것이 좋다.
```python
import heapq 
```

- #### heapq의 time complexity 
    * get item : O(1)
    * insert item : O(logn)
    * delete item : O(logn)
    * search item : O(n)

- #### heapq :: heapify
    주어진 리스트를 힙정렬한다.
    ```python
    import heapq 
    my_list = [1, 5, 3, 4]
    heapq.heapify(my_list)
    ```

- #### heapq :: heappush (logn)
    힙 정렬된 리스트의 힙 상태를 유지하면서 데이터를 삽입시킨다.
    (힙 정렬을 하지 않고 heappush시 이상하게 데이터가 구성된다.)
    ```python
    import heapq 
    my_list = [1, 5, 3, 4]
    heapq.heapify(my_list)
    heapq.heappush(my_list, 7)
    ```


- #### heapq :: heappop (logn)
    힙 정렬된 리스트의 가장 작은 원소를 빼내고 나머지 원소가 힙을 유지하도록 정리한다.
    (힙 정렬을 하지 않고 heappush시 이상하게 데이터가 구성된다.)
    ```python
    import heapq 
    my_list = [1, 5, 3, 4]
    heapq.heapify(my_list)
    print(my_list[0]) #힙 리스트에서 가장 작은 원소는 항상 [0]에 있다.
    print(heapq.heappop(my_list))
    ```

<br>
<br>