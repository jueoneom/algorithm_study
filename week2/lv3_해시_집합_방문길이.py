def solution(dirs):
    pos_set = set()
    X, Y = 0, 1
    dir_dict = {'U': (0,1), 'D': (0,-1), 'R':(1,0), 'L':(-1,0)}
    cur_pos = [0, 0]

    for dir in dirs:
        last_pos = cur_pos[:]
        cur_pos[X] += dir_dict[dir][X]
        cur_pos[Y] += dir_dict[dir][Y] 
        #boundary check   
        if -5 > cur_pos[X] or cur_pos[X] > 5:
            cur_pos[X] -= dir_dict[dir][X]
        if -5 > cur_pos[Y] or  cur_pos[Y] > 5:
            cur_pos[Y] -= dir_dict[dir][Y]
        #반복 check
        if last_pos != cur_pos and (tuple(cur_pos), tuple(last_pos)) not in pos_set:
            pos_set.add((tuple(last_pos),tuple(cur_pos)))
    
    return len(pos_set)


    '''
규칙
    1. 좌표평면을 넘어서면 안된다. -5 ~ 5
    2. 반복된 벡터(그 반대 벡터도 마찬가지)는 셈하지 않는다.
    
로직
    1. 집합을 사용한다. 앞 뒤 좌표를 튜플안에 같이 넣는 것으로 벡터 표현
        - 이 때 반대 벡터도 함께 넣어주어야한다!
    2. 만약 -5~5를 넘을 경우 무시한다.
    
'''


def solution(directions):
    DIRS = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}
    X, Y = 0, 1
    visited_set = set()
    location = [0, 0]
    for direction in directions:
        origin_x, origin_y = location
        if -5 <= location[X] + DIRS[direction][X] <= 5 and -5 <= location[Y] + DIRS[direction][Y] <= 5:   
            location[X] += DIRS[direction][X]
            location[Y] += DIRS[direction][Y]
            visited_set.add((origin_x, origin_y, location[X], location[Y]))
            visited_set.add((location[X], location[Y], origin_x, origin_y))
    
    return len(visited_set)/2