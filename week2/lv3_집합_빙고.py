def solution(board, nums):
    answer = 0
    num_set = set(nums)
    d1_set = set()
    d2_set = set()
    board_size = len(board)
    for j in range(board_size):
        h_set = set(board[j])
        v_set = set()
        for i in range(board_size):
            v_set.add(board[i][j])
            if j == i:
                d1_set.add(board[j][i])
            if i + j == board_size -1:
                d2_set.add(board[j][i])
        if not h_set - num_set:
            answer += 1
        if not v_set - num_set:
            answer += 1
    if len(d1_set) == board_size and not d1_set - num_set:
        answer += 1
    if len(d2_set) == board_size and not d2_set - num_set:
        answer += 1
    
            
    return answer