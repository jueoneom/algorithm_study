def solution(board, nums):
    SIZE = len(board) 

    answer = 0
    nums_set = set(nums) 
    diagonal_Lset = set() #첫번째 대각선 빙고 집합
    diagonal_Rset = set() #두번째 대각선 빙고 집합
    v_set = set() #세로 빙고 집합
    
    for j in range(SIZE):
        h_set = set(board[j]) #가로 빙고 집합
        v_set.clear()

        for i in range(SIZE):
            v_set.add(board[i][j])

            if j == i:
                diagonal_Lset.add(board[j][i])
            if i + j == SIZE -1:
                diagonal_Rset.add(board[j][i])
        
        if not h_set - nums_set:
            answer += 1
        if not v_set - nums_set:
            answer += 1

    if len(diagonal_Lset) == SIZE and not diagonal_Lset - nums_set:
        answer += 1
    if len(diagonal_Rset) == SIZE and not diagonal_Rset - nums_set:
        answer += 1
    
            
    return answer



    '''
규칙
    1. 가로, 세로 왼, 오 대각선 방향으로 빙고 
    2. 왼 대각선 규칙: x == y
    3. 오 대각선 규칙: x - y = n - 1
    4. 빙고 개수 리턴
로직 
    1. nums에 있는 빙고가 몇개 존재하는지 확인하면 된다.
    2. [0] * n (* 2)(가로, 세로엔 몇개씩 체크할 수 있는가?)
    3. [0] * 2 (대각선)
    4. for문을 돌려 nums가 있는지 확인해본다.
    5. 가로 세로, 대각선 리스트가 n개인 갯수를 구해 리턴하면 됨
'''


def solution(board, nums):
    n = len(board)
    row_count, col_count = [0] * n, [0] * n
    diagnal_count = [0] * 2
    nums = set(nums)
    
    for j, row in enumerate(board):
        for i, item in enumerate(row):
            if item in nums:
                row_count[i] += 1
                col_count[j] += 1
                if i == j:
                    diagnal_count[0] += 1
                if i + j == n - 1:
                    diagnal_count[1] += 1
                    
    return (row_count + col_count + diagnal_count).count(n)