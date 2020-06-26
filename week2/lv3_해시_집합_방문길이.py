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