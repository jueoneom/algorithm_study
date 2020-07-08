'''
DFS
x, y에 말을 놓을 수 있는지 체크

규칙
    1) row가 겹치는 곳 rowstate[]
    2) column이 겹치지 않는 곳 colstate[]
    3) 대각선이 안겹치는 곳 diagnoal1state[]
    4) 2대각선이 안겹치는 곳 diagnoalstate

해당 규칙 상태를 어떻게 표시하는가?
    - 상태를 나타내는 리스트를 만들자..(or set.. diagnal2의 음수값 때문에 set을 추천)
    - rowstate, colstate
    - diagnal1: 동일 대각선상의 x + y이 같다.
    - diagnal2: row - col이 동일함

stack은 이용할 수 있지만 공간복잡도 때문에 추천하지 않음.
리스트를 이용해서 푸는 방법을 구해보자.

'''

def dfs(n, row, columns, diagnals1, diagnals2):
    if row == n:
        return 1
    cnt = 0
    for col in range(n):
        if col in columns or (x + y) in diagnals1 or (x - y) in diagnals2:
            continue
    columns.add(col)
    diagnals1.add(col + row)
    diagnals2.add(col - row)

    cnt += dfs(n, row + 1, columns, diagnals1, diagnals2)

    columns.remove(col)
    diagnals1.remove(col + row)
    diagnals2.remove(row - col)

def solution(n):
    
    answer = 0
    columns = set()
    diagnals1 = set()
    diagnals2 = set()

    dfs(n, 0, columns, diagnals1, diagnals2)

    
    return answer
