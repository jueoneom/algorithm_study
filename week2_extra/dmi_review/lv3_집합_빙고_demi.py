'''
풀이법
보드칸을 가로/세로/대각선으로 순회하면서 for문이 2개가 필요하므로 O(n2)  
동그라미를 세주는 느낌
'''
#O(n3) 풀이방법, 효율성 테스트 0점임
'''
def solution(board, nums):
    N = len(nums)
    row_bingo_counts = [0] * N
    col_bingo_counts = [0] * N
    diagnoal_bingo_counts = [0] * 2

    for i, row in enumerate(board):
        for j, number in enumerate(row):
            if number in nums:
                row_bingo_counts[i] += 1
                col_bingo_counts[j] += 1

                if i == j:
                    diagnoal_bingo_counts[0] += 1
                if i+j == N -1:
                    diagnoal_bingo_counts[1] += 1
    answer += (row_bingo_counts + col_bingo_counts + diagnoal_bingo_counts).count(N)
    return answer
'''

#중복값을 찾을 때, 리스트 안에 뭐가 들어있어야 할지 알아야할 때, set이 좋다.

def solution(board, nums):
    N = len(nums)
    row_bingo_counts = [0] * N
    col_bingo_counts = [0] * N
    diagnoal_bingo_counts = [0] * 2
    nums = set(nums) # 집합으로 바꾸면 엄청 빨라짐!! 
    for i, row in enumerate(board):
        for j, number in enumerate(row):
            if number in nums:
                row_bingo_counts[i] += 1
                col_bingo_counts[j] += 1

                if i == j:
                    diagnoal_bingo_counts[0] += 1
                if i+j == N -1:
                    diagnoal_bingo_counts[1] += 1
    # N이 리스트 내에서 몇개 들어있는지 확인하는 메소드
    answer += (row_bingo_counts + col_bingo_counts + diagnoal_bingo_counts).count(N)
    return answer


    