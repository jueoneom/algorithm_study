'''
로직
지나온 길을 표시하는 set을 초기화 한다.
모든 명령어에 대해 
다음 방향으로 갈 수 있는지 검사한다.
    갈 수 없다면 무시한다
지나온 길을 set에 넣는다. 이 때, 원소를 두개 넣어줘야한다.
(점1의 x, 점1의 y, 점2의 x, 점2의 y)
(점2의 x, 점2의 y, 점1의 x, 점1의 y)
지나온 길(set)의 길이 / 2를 리턴한다.

time complexity : commands 길이만큼
'''
#refactoring
def is_valid(x, y):
    return -5 <= x <= 5 and -5 <= y <= 5

def solution(commands):
    visited_paths = set()
    
    cur_position = [0, 0]
    DELTAS = {'U': (0, 1), 'D': (0, -1), 'R':(1, 0), 'L':(-1, 0)}

    for command in commands:
        dy, dx = DELTAS[command]
        next_position = (cur_position[0] + dx, cur_position[1] + dy)
        x, y = next_position
        # if not (-5<=x<=5 and -5<=y<=5):
        if not is_valid(x, y):
            continue

        visited_paths.add(cur_position, next_position)
        visited_paths.add(next_position, cur_position)

    return len(visited_paths)

