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