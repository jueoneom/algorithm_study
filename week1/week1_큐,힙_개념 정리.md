# Python:: 큐, 힙 개념정리

<br>

### 문제 설명
---
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

- 구조대 : 119
- 박준영 : 97 674 223
- 지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

<br>

### 제한 사항
---
- phone_book의 길이는 1 이상 1,000,000 이하입니다.
- 각 전화번호의 길이는 1 이상 20 이하입니다.

<br>

### 제출 코드
---
```python
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]:
            return False
    return True
```

<br>

### 문제 풀이
---

전달받은 인자 `phone_book`의 원소들이 `str` 값이니 이를 이용하여 `sorting`을 진행한다.

그러면 같은 문자로 시작하는 숫자들 순으로 정렬이 되므로 접두어 포함 여부를 확인하기 수월하다.

이후 반복을 진행하여 접두어 포함 여부를 확인하여 결과에 따라 적절한 값을 반환한다.

\
