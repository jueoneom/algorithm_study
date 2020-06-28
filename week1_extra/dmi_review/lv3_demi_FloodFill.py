#demi's code
'''
* 로직 (코드 작성시 꼭 로직을 작성하자!) 
    1. 모든 좌표를 방문할 때까지 다음을 반복한다.
        1. 방문하지 않은 좌표를 발견하면
        2. 큐에 해당 좌표를 넣고
        3. 큐가 빌때까지 다음을 반복한다.
            1. 큐에서 원소 하나를 꺼낸 후
            2. 방문했다고 표시
            3. 상하좌우로 같은 색인 좌표를 큐에 넣기
'''

from collections import deque
def solution(n, m, image):
    #먼저 필요한 변수 선언
    answer = 0
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                answer += 1
                visited[i][j] = True
                bfs(n,m,i,j, image, visited)
            
    return answer


def bfs(n, m, x, y, image, visited):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft() #unpacking임 
        vistied[x][y] = True

        #변화량을 상수로 정의해줌(상, 하, 좌, 우) 리스트는 가변적인 값이라 튜플이 더 좋다.
        DELTAS = ((0,1), (0,-1),(1,0),(-1,0))
        for dx, dy in DELTAS:
            next_x, next_y = x+dx, y+dy
            #boundary check (중요)
            #리팩토링 전 후(visitable 함수)
            # if not (0 <= next_x < n and 0 <= next_y < m and not visited[next_x][next_y]):
            #     continue
            if visitable(next_x, next_y) and image[next_x][next_y] == image[x][y]:
                queue.append({next_x, next_y})
                visited[next_x][next_y] 

#리팩토링은 시간이 남을 때! 우선은 통과하는 코드다! 자신있을 때 함수로 별도로 빼기
#리팩토링 후
def visitable(n, m, x, y, visited):
    return 0 <= next_x < n and 0 <= next_y < m and not visited[next_x][next_y]
