'''
1. 로직
    1. 규칙 1 ~ 4에 해당하는 col, left_d, right_d 리스트 혹은 셋을 정의한다.
    2. 각 행 인덱스 m을 매개변수로 받는 search_queen 함수를 정의한다.
        1. m이 n일 경우 1을 리턴한다. 
        2. result를 정의한다
        3. search_queen 함수 내에서 for문을 돌며 열을 탐색한다.
            1. 해당 col이 T 인지 F 인지 확인한다.
            2. 해당 left_d가 T 인지 F 인지 확인함
            3. right_d가 T 인지 F 인지 확인한다.
                1. 3개의 조건이 모두 T일 경우 queen을 두고 모두 F로 바꾼다.
                2. 다음 행을 확인하기 위해 search_queen(m+1)을 호출한다. 리턴 값을 result에 더한다.
2. 시간 복잡도
    O(N!): m이 커질수록 search_queen() 호출 수가 N번, N-1, ...1번으로 줄어든다. 이를 시간 복잡도로 표현하면 O(N!)
'''


#리스트를 이용한 풀이


def solution(n):
    
    col = [True] * n
    diagnal_left = [True] * (2 * n - 1)
    diagnal_right = [True] * (2 * n - 1)
    return search_queen(0, n, col, diagnal_left, diagnal_right)

def search_queen(m, n, col, diagnal_left, diagnal_right):
    if m == n:
        return 1
    result = 0
    for i in range(n):
        if not col[i] or not diagnal_left[m + i] or not diagnal_right[m - i + n - 1]: continue
        col[i] = False
        diagnal_left[m + i] = False
        diagnal_right[m - i + n - 1] = False
        result += search_queen(m + 1, n, col, diagnal_left, diagnal_right)
        col[i] = True
        diagnal_left[m + i] = True
        diagnal_right[m - i + n - 1] = True
    return result
        
        
n = int(input())
print(solution(n))




