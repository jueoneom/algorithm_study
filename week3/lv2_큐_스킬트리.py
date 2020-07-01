from collections import deque
def solution(skill, skill_trees):
    answer = 0
    skill_set = set(skill)
    
    que = deque()
    for tree in skill_trees:
        que.clear()
        
        for s in tree:
            if s in skill_set:
                que.append(s)
                
        is_skill = True
        for s in skill:
            if que and s != que.popleft():
                is_skill = False
                break
        if is_skill:
            answer += 1
                
    return answer