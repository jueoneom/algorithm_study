#DFS
def solution(numbers, target):
    NUM_SUM, NUM_IDX = 0, 1
    answer = 0
    stack = [(0, 0)]
    
    while stack:
        num_sum, num_idx = stack.pop()
        if num_idx == len(numbers):
            if num_sum == target:
                answer += 1
        else:
            stack.append((num_sum - numbers[num_idx], num_idx+1))
            stack.append((num_sum + numbers[num_idx], num_idx+1))
        
    
    return answer