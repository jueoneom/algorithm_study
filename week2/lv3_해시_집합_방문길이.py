def solution(dirs):
    answer = 0
    pos_set = set()
    cur_pos = [0, 0]
    dir_dict = {'U': (0,1), 'D': (0,-1), 'R':(1,0), 'L':(-1,0)}
    for dir in dirs:
        last_pos = cur_pos[:]
        cur_pos[0] += dir_dict[dir][0]
        cur_pos[1] += dir_dict[dir][1]
        
        if -5 > cur_pos[0] or cur_pos[0]> 5:
            cur_pos[0] -= dir_dict[dir][0]
        if -5 > cur_pos[1] or  cur_pos[1]> 5:
            cur_pos[1] -= dir_dict[dir][1]
            
        if last_pos != cur_pos and (tuple(cur_pos), tuple(last_pos)) not in pos_set:
            
            pos_set.add((tuple(last_pos),tuple(cur_pos)))
    
    return len(pos_set)